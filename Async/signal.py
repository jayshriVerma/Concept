import asyncio
import signal
import sys

# Example async resource
# Async Cleanup with asyncio and Signal Handling
class DummyAsyncService:
    async def start(self):
        print("Async service started")
    async def stop(self):
        print("Async service stopped")

# Create global service
service = DummyAsyncService()

shutdown_event = asyncio.Event()

async def main():
    # Start resource
    await service.start()
    print("Running... Press Ctrl+C to stop.")

    # Wait until shutdown signal is received
    await shutdown_event.wait()

    # Cleanup before exit
    print("Running async cleanup...")
    await service.stop()
    print("Cleanup done. Exiting now.")

def handle_signal(signum, frame):
    print(f"\n🔹 Caught signal: {signum}")
    shutdown_event.set()  # wake up main()

if __name__ == "__main__":
    # Register signals
    signal.signal(signal.SIGINT, handle_signal)   # Ctrl+C
    signal.signal(signal.SIGTERM, handle_signal)  # kill/terminate

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # Fallback (shouldn’t normally trigger because we catch SIGINT)
        print("\nInterrupted, exiting...")
        sys.exit(0)
