from dhooks import Webhook

hook = Webhook("Enter your webhook")

while 1:
  msg = input("Enter your desired message")
  hook.send(msg)


