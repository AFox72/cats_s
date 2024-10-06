application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            url(r'^ws/messages/(?P<recipient>\w+)/$', MessagesConsumer),
        ])
    ),
})
