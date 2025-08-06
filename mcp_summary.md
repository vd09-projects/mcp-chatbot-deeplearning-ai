# Model Context Protocol (MCP) Architecture

This overview of the Model Context Protocol (MCP) discusses its scope and core concepts, and provides examples demonstrating each core concept.

## Scope

The Model Context Protocol includes the following projects:

* MCP Specification: A specification of MCP that outlines the implementation requirements for clients and servers.
* MCP SDKs: SDKs for different programming languages that implement MCP.
* MCP Development Tools: Tools for developing MCP servers and clients, including the MCP Inspector
* MCP Reference Server Implementations: Reference implementations of MCP servers.

## Concepts of MCP

### Participants

MCP follows a client-server architecture with three key participants:

* **MCP Host**: The AI application that coordinates and manages one or multiple MCP clients
* **MCP Client**: A component that maintains a connection to an MCP server and obtains context from an MCP server for the MCP host to use
* **MCP Server**: A program that provides context to MCP clients

Each MCP host establishes connections to one or more MCP servers by creating one MCP client for each MCP server. Each MCP client maintains a dedicated one-to-one connection with its corresponding MCP server.

MCP servers can execute locally or remotely:
- **Local MCP servers**: Run on the same machine (e.g., filesystem server using STDIO transport)
- **Remote MCP servers**: Run on a different machine (e.g., Sentry MCP server using Streamable HTTP transport)

### Layers

MCP consists of two layers:

1. **Data Layer**: Defines the JSON-RPC based protocol for client-server communication, including:
   - Lifecycle management
   - Core primitives (tools, resources, prompts)
   - Client features
   - Utility features

2. **Transport Layer**: Defines the communication mechanisms between clients and servers:
   - Stdio transport: Uses standard input/output streams for local process communication
   - Streamable HTTP transport: Uses HTTP POST for remote server communication with optional Server-Sent Events

### Data Layer Protocol

The data layer uses JSON-RPC 2.0 as its underlying RPC protocol, with clients and servers sending requests to each other and responding accordingly.

#### Lifecycle Management

MCP requires lifecycle management to negotiate the capabilities that both client and server support.

#### Primitives

MCP defines three core primitives that servers can expose:

* **Tools**: Executable functions that AI applications can invoke to perform actions
* **Resources**: Data sources that provide contextual information to AI applications
* **Prompts**: Reusable templates that help structure interactions with language models

Each primitive type has associated methods for discovery (`*/list`), retrieval (`*/get`), and in some cases, execution (`tools/call`).

MCP also defines primitives that clients can expose:

* **Sampling**: Allows servers to request language model completions from the client's AI application
* **Elicitation**: Allows servers to request additional information from users
* **Logging**: Enables servers to send log messages to clients for debugging and monitoring purposes

#### Notifications

The protocol supports real-time notifications to enable dynamic updates between servers and clients. Notifications are sent as JSON-RPC 2.0 notification messages and enable MCP servers to provide real-time updates to connected clients.