import os

# Optional import tolerance to allow local runs without OTel installed
try:
    from opentelemetry import trace
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
except Exception:  # pragma: no cover - graceful degradation
    trace = None
    Resource = None
    TracerProvider = None
    OTLPSpanExporter = None
    BatchSpanProcessor = None


def init_tracing(service_name: str = "codex-api") -> None:
    """Initialize OpenTelemetry tracing if dependencies are available."""
    if trace is None:
        # OTel not installed; noop
        return
    endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317")
    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource)
    # insecure=True permits http endpoint
    exporter = OTLPSpanExporter(endpoint=endpoint, insecure=True)
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)
