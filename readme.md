# 🛡️ Railgun MCP Server

[![PyPI Version](https://img.shields.io/pypi/v/railgun-mcp.svg)](https://pypi.org/project/railgun-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/pypi/pyversions/railgun-mcp.svg)](https://pypi.org/project/railgun-mcp/)

A comprehensive Model Context Protocol (MCP) server for interacting with the **Railgun privacy protocol**. This server enables AI assistants and other MCP clients to perform **private DeFi transactions** on Ethereum, Arbitrum, Polygon, and BSC with zero-knowledge privacy guarantees.

## ✨ Features

### 🔐 **Complete Privacy Suite**
- **Wallet Management** - Create, import, and manage Railgun wallets with both public (0x) and private (0zk) addresses
- **Private Transactions** - Send tokens privately between 0zk addresses with zero-knowledge proofs
- **Shield/Unshield** - Move tokens between public and private balances seamlessly
- **Multi-Wallet Operations** - Batch operations, token distribution, and privacy mixing

### 🧩 **Advanced DeFi Integration**
- **Recipe System** - Create and execute complex DeFi operations privately
- **Private Swaps** - Trade tokens without revealing amounts or addresses
- **Relayer Network** - Enhanced privacy through decentralized relayer integration
- **Gas Optimization** - Smart gas estimation and transaction batching

### 🤖 **Plain-English AI Tools**
- **Smart Affordability Checker** - "Can I afford this transaction?"
- **Cost Explainer** - "Why is this so expensive?"
- **Simple Money Sending** - "Just send 100 USDC to alice.eth privately"
- **Token Finder** - "Where are my tokens?"
- **Privacy Optimizer** - "How can I be more private?"
- **Emergency Exit** - "Get all my funds out quickly"

### 🌐 **Multi-Network Support**
- **Ethereum** - Full feature support
- **Arbitrum** - L2 privacy with low fees
- **Polygon** - Fast and cheap private transactions
- **BSC** - Binance Smart Chain integration

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI (recommended)
pip install railgun-mcp

# Or install from source
git clone https://github.com/railgun-org/railgun-mcp.git
cd railgun-mcp
pip install -e .
```

### Configuration

**Option 1: Environment Variables**
```bash
export RAILGUN_PRIVATE_KEY="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
export RAILGUN_WALLET_PASSWORD="your-secure-password"
export ETHEREUM_RPC_URL="https://eth-mainnet.g.alchemy.com/v2/your-key"
```

**Option 2: Config File**
Create `~/.railgun/config.json`:
```json
{
  "private_key": "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
  "wallet_password": "your-secure-wallet-password",
  "rpc_endpoints": {
    "ethereum": "https://eth-mainnet.g.alchemy.com/v2/your-key",
    "arbitrum": "https://arb-mainnet.g.alchemy.com/v2/your-key",
    "polygon": "https://polygon-mainnet.g.alchemy.com/v2/your-key"
  }
}
```

**Option 3: Claude Desktop Configuration**
See [`examples/CLAUDE_DESKTOP_SETUP.md`](./examples/CLAUDE_DESKTOP_SETUP.md) for detailed Claude Desktop setup instructions.

### Run the Server

```bash
# Start the MCP server
python -m railgun_mcp

# Or use the command line tool
railgun-mcp
```

### Connect with MCP Client (Claude Desktop)

Add to your Claude Desktop configuration (`~/Library/Application Support/Claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "railgun-mcp": {
      "command": "python",
      "args": ["-m", "railgun_mcp"],
      "env": {
        "RAILGUN_PRIVATE_KEY": "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        "RAILGUN_WALLET_PASSWORD": "your-secure-password",
        "ETHEREUM_RPC_URL": "https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY"
      }
    }
  }
}
```

**⚠️ Important**: Replace the example private key with your actual wallet private key.

**📋 For detailed setup instructions**: See [`examples/CLAUDE_DESKTOP_SETUP.md`](./examples/CLAUDE_DESKTOP_SETUP.md)

## 🛠️ Available Tools

### 👛 **Wallet Management**
- `create_wallet` - Create a new Railgun wallet
- `import_wallet` - Import existing wallet from private key
- `list_wallets` - List all configured wallets
- `create_wallet_batch` - Create multiple wallets for enhanced privacy

### 💰 **Balance & Transactions**
- `get_balance` - Check public and private balances
- `shield_tokens` - Move tokens to private balance
- `unshield_tokens` - Move tokens to public balance  
- `private_transfer` - Transfer between 0zk addresses
- `get_transaction_history` - View transaction history
- `distribute_tokens` - Distribute tokens across multiple wallets

### 🔄 **DeFi Operations**
- `create_recipe` - Create custom DeFi recipes
- `execute_recipe` - Execute recipes privately
- `create_swap_recipe` - Pre-built swap recipes
- `estimate_recipe_gas` - Estimate gas costs

### 🤖 **AI-Friendly Tools**
- `can_i_afford_this` - Check if you can afford an action
- `why_is_this_so_expensive` - Explain transaction costs
- `just_send_money` - Send money the easiest way
- `where_are_my_tokens` - Find all your tokens
- `fix_stuck_transaction` - Help with stuck transactions
- `optimize_my_privacy` - Get privacy improvement tips
- `emergency_exit` - Quick fund extraction

### 🌐 **Network & Utilities**
- `get_relayers` - Find available relayers
- `get_supported_tokens` - List supported tokens
- `check_config` - Verify configuration
- `verify_proof` - Verify zero-knowledge proofs

## 📖 Usage Examples

### Basic Wallet Operations
```python
# Create a wallet
create_wallet(network="ethereum", password="secure-password")

# Shield tokens into private balance  
shield_tokens(
    wallet_id="wallet-123",
    token_address="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # USDC
    amount="1000000000"  # 1000 USDC
)

# Private transfer
private_transfer(
    wallet_id="wallet-123", 
    token_address="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    amount="500000000",  # 500 USDC
    recipient_0zk_address="0zk1234..."
)
```

### AI-Friendly Operations
```python
# Simple English commands
can_i_afford_this(wallet_id="wallet-123", action="swap", amount="1000", token="USDC")

just_send_money(
    wallet_id="wallet-123",
    to="alice.eth", 
    amount="100 USDC",
    keep_private=True
)

where_are_my_tokens(wallet_id="wallet-123")
```

### Advanced Privacy Features
```python
# Create multiple wallets for privacy
create_wallet_batch(count=5, network="ethereum", password_prefix="secure")

# Distribute tokens across wallets
distribute_tokens(
    source_wallet_id="wallet-123",
    token_address="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    total_amount="5000000000",  # 5000 USDC
    destination_wallet_ids=["wallet-124", "wallet-125", "wallet-126"],
    distribution_type="equal"
)

# Mix tokens for enhanced privacy
mix_tokens(
    wallet_ids=["wallet-123", "wallet-124", "wallet-125"],
    token_address="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    mixing_rounds=3
)
```

## 🔒 Security Best Practices

- **Never commit API keys or private keys** to version control
- **Use environment variables** or secure config files for sensitive data
- **Always verify transaction details** before execution
- **Keep wallet passwords secure** and use strong, unique passwords
- **Enable 2FA** on all related accounts (RPC providers, etc.)
- **Regular security audits** of your configuration

## 🧪 Development

```bash
# Clone the repository
git clone https://github.com/railgun-org/railgun-mcp.git
cd railgun-mcp

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black railgun_mcp/
isort railgun_mcp/

# Type checking
mypy railgun_mcp/

# Run with debug logging
export LOG_LEVEL=DEBUG
python -m railgun_mcp
```

## 📚 Documentation

- **[Installation Guide](./docs/installation.md)** - Detailed setup instructions
- **[Configuration Guide](./docs/configuration.md)** - All configuration options
- **[API Reference](./docs/api.md)** - Complete tool documentation
- **[Privacy Guide](./docs/privacy.md)** - Best practices for privacy
- **[Examples](./examples/)** - Code examples and tutorials

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](./CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Run the test suite
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🔗 Links

- **[Railgun Protocol](https://railgun.org)** - Official Railgun website
- **[Documentation](https://docs.railgun.org)** - Complete protocol documentation  
- **[Discord Community](https://discord.gg/railgun)** - Join the community
- **[GitHub Issues](https://github.com/railgun-org/railgun-mcp/issues)** - Report bugs and request features

## ⚠️ Disclaimer

This software is provided "as is" without warranties. Always verify transactions and use at your own risk. The Railgun protocol is experimental technology - please understand the risks before using with significant funds.
