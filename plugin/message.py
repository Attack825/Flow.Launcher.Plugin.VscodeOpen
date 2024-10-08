import urllib.parse

from log_config import setup_logging
from utils import Project

setup_logging()


class MessageDTO:
    """消息传输对象"""

    def __init__(
        self,
        title: str = "title",
        subtitle: str = "subtitle",
        icopath: str = "images/app.png",
        method: str = "open_url",
        parameters: list[str] = [""],
    ) -> None:
        self.title = title
        self.subtitle = subtitle
        self.icopath = icopath
        self.method = method
        self.parameters = parameters

    def asFlowMessage(self) -> list:
        return [
            {
                "Title": urllib.parse.unquote(self.title),
                "SubTitle": self.subtitle,
                "IcoPath": self.icopath,
                "jsonRPCAction": {
                    "method": self.method,
                    "parameters": self.parameters,
                },
            }
        ]

    @staticmethod
    def asMultiFlowMessage(
        projects: list[Project], icopath, method: str, app_download: str
    ):
        message_list = []

        titles = [project.name for project in projects]
        subtitles = [project.path for project in projects]
        parameters = []
        for project in projects:
            parameter = [" ".join([app_download, project.path])]
            parameters.append(parameter)

        for i in range(len(titles)):
            message_list.append(
                {
                    "Title": titles[i],  # unquote指示中文转码
                    "SubTitle": subtitles[i],
                    "IcoPath": icopath,
                    "jsonRPCAction": {
                        "method": method,
                        "parameters": parameters[i],
                    },
                }
            )
        return message_list

    @staticmethod
    def asWarnFlowMessage(msg, operation) -> list:
        return [
            {
                "Title": msg,
                "SubTitle": operation,
                "IcoPath": "icons/app.png",
            }
        ]

    @staticmethod
    def asDebugFlowMessage(msg) -> list:
        return [
            {
                "Title": msg,
                "SubTitle": "Debug",
                "IcoPath": "icons/warn.png",
            }
        ]
