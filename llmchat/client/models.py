from kubernetes import client
from kubernetes.client import CustomObjectsApi

from llmchat.client.consts import group, version, openmodel_plural


def get_openmodel_objects(api: CustomObjectsApi, namespace: None):
    try:
        if namespace:
            # TODO: we do not support namespaced models yet.
            raise NotImplementedError("do not support namespaced models yet")
        else:
            response = api.list_cluster_custom_object(
                group=group,
                version=version,
                plural=openmodel_plural,
            )
        return response.get("items", [])
    except client.exceptions.ApiException as e:
        print(f"Error fetching OpenModel objects: {e}")
        return []
