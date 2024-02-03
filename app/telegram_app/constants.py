from typing import Optional

from pydantic import BaseModel


class UpdateSchema(BaseModel):
    update_id: int
    message: Optional[dict] = None
    edited_message: Optional[dict] = None
    channel_post: Optional[dict] = None
    edited_channel_post: Optional[dict] = None
    message_reaction: Optional[dict] = None
    message_reaction_count: Optional[dict] = None
    inline_query: Optional[dict] = None
    chosen_inline_result: Optional[dict] = None
    callback_query: Optional[dict] = None
    shipping_query: Optional[dict] = None
    pre_checkout_query: Optional[dict] = None
    poll: Optional[dict] = None



WELLCOME_MESSAGE = """Hola {first_name}!

Welcome to WeRise Bot!

WeRise is a platform that helps you manage your crowd funding campaign. Anyone can create a campaign and raise funds for their cause.

If you want to create a campaign, Please click /verify to verify your identity.

Donators can donate without verifying their identity or creating an account.

For more information and help center, Please click /help
"""

# /start command but not the first time
START_COMMAND = """Hola {first_name}!

Welcome back to WeRise Bot!

What can i help you today?

For more information and help center, Please click /help
"""

# /help command
HELP_COMMAND = """WeRise Bot Help Center

/start - Start the bot.
/help - Help center.
/about - About WeRise Bot.

/create_campaign - Create a campaign.
/my_campaigns - List all your campaigns.

/verify - Verify your identity.
/donate - Donate to a campaign.

/withdraw - Withdraw funds from your campaign.
/withdraw_history - List all your withdraws.

/contact - Contact us.

/privacy - Terms and conditions.
/delete_account - Delete your account.
"""

VERIFY_IDENTIFY = """Our verification process is very simple. Please follow the steps below.

1. Click /verify
2. It will take you to our website and agree to our terms and conditions.
3. Upload your identity card and selfie.
4. Wait for our team to verify your identity.
5. Once verified, You can create campaigns and withdraw funds.

If you have any questions, Please click /contact

"""

# instructions to use private chat only
USE_ONLY_PRIVATE_CHAT = """Please use this command in private chat."""

# document recieved message
DOCUMENT_RECIEVED = """Dear {first_name},

We want to inform you that we have recieved your documents and we are currently verifying your identity.

We will notify you once your identity is verified.

Thank you for your patience.
Team WeRise
"""