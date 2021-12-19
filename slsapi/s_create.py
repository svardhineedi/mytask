import serverless_sdk
sdk = serverless_sdk.SDK(
    org_id='svardhineedi',
    application_name='slsapi',
    app_uid='sWKlXqH3dJNMLj11Xw',
    org_uid='e18a477d-050a-46bc-9f8f-8b83bcfbb6d9',
    deployment_uid='187c500a-6ae0-4ddc-b2f7-5d952e6be4d2',
    service_name='slsapi',
    should_log_meta=True,
    should_compress_logs=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name='dev',
    plugin_version='5.5.1',
    disable_frameworks_instrumentation=False,
    serverless_platform_stage='prod'
)
handler_wrapper_kwargs = {'function_name': 'slsapi-dev-create', 'timeout': 6}
try:
    user_handler = serverless_sdk.get_user_handler('/user.save')
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error
    def error_handler(event, context):
        raise e
    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
