from google.adk.artifacts import BaseArtifactService
from google.genai import types
import magic
import os
from typing import Optional
import base64

class DiskArtifactSerivce(BaseArtifactService):
    def __init__(self, base_dir):
        if not os.path.exists(base_dir):
            os.makedirs(base_dir, exist_ok=True)

        self.base_dir = base_dir

    def makedirs_if_not_exists(self, session_id):
        path = os.path.join(self.base_dir, session_id)
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        return path

    def list_artifact_keys(self, *, app_name, user_id, session_id):
        # path = self.makedirs_if_not_exists(session_id)
        path = self.base_dir
        print("Listing artifacts in path: " + path + " ...")
        print("os.listdir result:")
        print(os.listdir(path))
        return os.listdir(path)

    def load_artifact(
        self,
        *,
        app_name: str,
        user_id: str,
        session_id: str,
        filename: str,
        version: Optional[int] = None,
    ):
        # path = self.makedirs_if_not_exists(session_id)
        path = self.base_dir
        path = os.path.join(path, filename)
        mime_type = magic.Magic(mime=True).from_file(path)
        with open(path, "rb") as f:
            
            return types.Part(
                inline_data=types.Blob(data=base64.b64encode(f.read()).decode("utf-8"), mime_type=mime_type),
            )

        return None

    def save_artifact(
        self,
        *,
        app_name: str,
        user_id: str,
        session_id: str,
        filename: str,
        artifact: types.Part,
    ) -> int:
        pass

    def list_versions(
        self, *, app_name: str, user_id: str, session_id: str, filename: str
    ) -> list[int]:
        pass

    def delete_artifact(
        self, *, app_name: str, user_id: str, session_id: str, filename: str
    ) -> None:
        pass