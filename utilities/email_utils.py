import os
import platform as os_platform
import base64
from pathlib import Path


# ============================================================
# COMMON EMAIL CONTENT
# ============================================================

def build_email_content(
    test_platform,
    total_tests,
    passed_tests,
    failed_tests
):

    platform_name = (
        "iOS"
        if test_platform.lower() == "ios"
        else "Android"
    )

    pass_percentage = (
        round((passed_tests / total_tests) * 100, 2)
        if total_tests > 0
        else 0
    )

    status = (
        "PASSED"
        if failed_tests == 0
        else "FAILED"
    )

    subject = (
        f"OVMS {platform_name} Automation "
        f"Test Execution Report - {status}"
    )

    html_body = f"""
    <html>
    <body>

    <p>Hi Team,</p>

    <p>
        The OVMS <b>{platform_name}</b> automation
        test execution has been completed.
    </p>

    <h3>Execution Summary</h3>

    <table border="1"
           cellpadding="7"
           cellspacing="0"
           style="border-collapse: collapse;">

        <tr>
            <td><b>Platform</b></td>
            <td>{platform_name}</td>
        </tr>

        <tr>
            <td><b>Execution Type</b></td>
            <td>Automation</td>
        </tr>

        <tr>
            <td><b>Framework</b></td>
            <td>Appium + Python + Pytest</td>
        </tr>

        <tr>
            <td><b>Total Test Cases</b></td>
            <td>{total_tests}</td>
        </tr>

        <tr>
            <td><b>Passed</b></td>
            <td>{passed_tests}</td>
        </tr>

        <tr>
            <td><b>Failed</b></td>
            <td>{failed_tests}</td>
        </tr>

        <tr>
            <td><b>Pass Percentage</b></td>
            <td>{pass_percentage}%</td>
        </tr>

        <tr>
            <td><b>Overall Status</b></td>
            <td><b>{status}</b></td>
        </tr>

    </table>

    <p>
        Please find the attached {platform_name}
        automation test execution report for your reference.
    </p>

    <p>
        Regards,<br>
        QA Team
    </p>

    </body>
    </html>
    """

    return platform_name, status, subject, html_body


# ============================================================
# WINDOWS - CLASSIC OUTLOOK
# ============================================================

def send_via_windows_outlook(
    subject,
    html_body,
    report_path,
    recipients
):

    try:

        import win32com.client as win32

        outlook = win32.Dispatch(
            "Outlook.Application"
        )

        mail = outlook.CreateItem(0)

        mail.To = ";".join(recipients)

        mail.Subject = subject

        mail.HTMLBody = html_body

        mail.Attachments.Add(
            str(report_path)
        )

        mail.Send()

        print(
            "✅ Report email sent through Classic Outlook"
        )

        return True

    except Exception as e:

        print(
            "❌ Failed to send email through Outlook"
        )

        print(
            "Error:",
            e
        )

        return False


# ============================================================
# MAC - MICROSOFT GRAPH
# ============================================================

def send_via_microsoft_graph(
    subject,
    html_body,
    report_path,
    recipients
):

    try:

        import msal
        import requests

        # ----------------------------------------------------
        # Azure / Microsoft Entra configuration
        # ----------------------------------------------------

        client_id = os.getenv(
            "MS_CLIENT_ID"
        )

        tenant_id = os.getenv(
            "MS_TENANT_ID"
        )

        if not client_id:

            raise ValueError(
                "MS_CLIENT_ID environment variable is missing"
            )

        if not tenant_id:

            raise ValueError(
                "MS_TENANT_ID environment variable is missing"
            )

        authority = (
            f"https://login.microsoftonline.com/{tenant_id}"
        )

        scopes = [
            "Mail.Send"
        ]

        # ----------------------------------------------------
        # MSAL Public Client
        # ----------------------------------------------------

        app = msal.PublicClientApplication(
            client_id=client_id,
            authority=authority
        )

        # ----------------------------------------------------
        # Try existing cached account
        # ----------------------------------------------------

        accounts = app.get_accounts()

        result = None

        if accounts:

            result = app.acquire_token_silent(
                scopes=scopes,
                account=accounts[0]
            )

        # ----------------------------------------------------
        # Device Login if token not available
        # ----------------------------------------------------

        if not result:

            flow = app.initiate_device_flow(
                scopes=scopes
            )

            if "user_code" not in flow:

                raise Exception(
                    "Unable to start Microsoft login"
                )

            print("")
            print(
                "=============================================="
            )

            print(
                "Microsoft 365 authentication required"
            )

            print(
                flow["message"]
            )

            print(
                "=============================================="
            )

            result = app.acquire_token_by_device_flow(
                flow
            )

        # ----------------------------------------------------
        # Validate token
        # ----------------------------------------------------

        access_token = result.get(
            "access_token"
        )

        if not access_token:

            raise Exception(
                result.get(
                    "error_description",
                    "Unable to obtain Microsoft Graph token"
                )
            )

        # ----------------------------------------------------
        # Read HTML report
        # ----------------------------------------------------

        with open(
            report_path,
            "rb"
        ) as report_file:

            report_content = base64.b64encode(
                report_file.read()
            ).decode("utf-8")

        # ----------------------------------------------------
        # Recipient Payload
        # ----------------------------------------------------

        to_recipients = []

        for recipient in recipients:

            to_recipients.append(
                {
                    "emailAddress": {
                        "address": recipient
                    }
                }
            )

        # ----------------------------------------------------
        # Graph Email Payload
        # ----------------------------------------------------

        payload = {

            "message": {

                "subject": subject,

                "body": {
                    "contentType": "HTML",
                    "content": html_body
                },

                "toRecipients": to_recipients,

                "attachments": [
                    {
                        "@odata.type":
                            "#microsoft.graph.fileAttachment",

                        "name":
                            report_path.name,

                        "contentType":
                            "text/html",

                        "contentBytes":
                            report_content
                    }
                ]
            },

            "saveToSentItems": True
        }

        # ----------------------------------------------------
        # Send Mail
        # ----------------------------------------------------

        headers = {
            "Authorization":
                f"Bearer {access_token}",

            "Content-Type":
                "application/json"
        }

        response = requests.post(
            "https://graph.microsoft.com/v1.0/me/sendMail",
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 202:

            print(
                "✅ Report email sent through Microsoft 365"
            )

            return True

        print(
            "❌ Microsoft Graph email failed"
        )

        print(
            "Status:",
            response.status_code
        )

        print(
            "Response:",
            response.text
        )

        return False

    except Exception as e:

        print(
            "❌ Failed to send email through Microsoft Graph"
        )

        print(
            "Error:",
            e
        )

        return False


# ============================================================
# COMMON SEND FUNCTION
# ============================================================

def send_test_report(
    platform,
    total_tests,
    passed_tests,
    failed_tests,
    report_path,
    recipients
):

    report_file = Path(
        report_path
    ).resolve()

    if not report_file.exists():

        print(
            f"❌ Report not found: {report_file}"
        )

        return False

    (
        platform_name,
        status,
        subject,
        html_body
    ) = build_email_content(
        test_platform=platform,
        total_tests=total_tests,
        passed_tests=passed_tests,
        failed_tests=failed_tests
    )

    print("")
    print(
        "=============================================="
    )

    print(
        "AUTOMATION REPORT EMAIL"
    )

    print(
        "=============================================="
    )

    print(
        "Platform :",
        platform_name
    )

    print(
        "Status   :",
        status
    )

    print(
        "Report   :",
        report_file
    )

    print(
        "Recipients:",
        ", ".join(recipients)
    )

    print(
        "=============================================="
    )

    operating_system = os_platform.system()

    # --------------------------------------------------------
    # Windows -> Classic Outlook
    # --------------------------------------------------------

    if operating_system == "Windows":

        return send_via_windows_outlook(
            subject=subject,
            html_body=html_body,
            report_path=report_file,
            recipients=recipients
        )

    # --------------------------------------------------------
    # macOS -> Microsoft Graph
    # --------------------------------------------------------

    elif operating_system == "Darwin":

        return send_via_microsoft_graph(
            subject=subject,
            html_body=html_body,
            report_path=report_file,
            recipients=recipients
        )

    else:

        print(
            f"❌ Unsupported operating system: {operating_system}"
        )

        return False