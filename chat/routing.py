from channels import include
from channels import route


channel_routing = [
	include("messanger.routing.websocket_routing", path=r"^/messanger/stream"),
	include("messanger.routing.custom_routing"),
]