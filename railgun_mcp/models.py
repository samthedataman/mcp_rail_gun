#!/usr/bin/env python3
"""
Models and data structures for Railgun MCP Server
"""

import json
import os
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


# Enums for Railgun types
class TokenType(Enum):
    ERC20 = "ERC20"
    ERC721 = "ERC721"
    NATIVE = "NATIVE"


class StepType(Enum):
    APPROVE = "approve"
    SWAP = "swap"
    TRANSFER = "transfer"
    SHIELD = "shield"
    UNSHIELD = "unshield"
    ADD_LIQUIDITY = "add_liquidity"
    REMOVE_LIQUIDITY = "remove_liquidity"
    STAKE = "stake"
    UNSTAKE = "unstake"


class Network(Enum):
    ETHEREUM = "ethereum"
    ARBITRUM = "arbitrum"
    POLYGON = "polygon"
    BSC = "bsc"


class TransactionStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    FAILED = "failed"
    CANCELLED = "cancelled"


# Data classes
@dataclass
class Token:
    address: str
    symbol: str
    decimals: int
    type: TokenType
    chain_id: int


@dataclass
class TokenAmount:
    token: Token
    amount: str  # Wei amount as string


@dataclass
class Step:
    id: str
    type: StepType
    description: str
    inputs: List[TokenAmount]
    outputs: List[TokenAmount]
    contract_address: Optional[str] = None
    function_name: Optional[str] = None
    function_args: Optional[Dict[str, Any]] = None


@dataclass
class Recipe:
    id: str
    name: str
    description: str
    steps: List[Step]
    network: Network
    created_at: str


# Configuration
class Config:
    """Configuration management for Railgun MCP"""

    def __init__(self):
        # Try to load from environment variables first
        self.api_key = os.getenv("RAILGUN_API_KEY")
        self.wallet_password = os.getenv("RAILGUN_WALLET_PASSWORD")
        self.rpc_endpoints = {
            "ethereum": os.getenv(
                "ETHEREUM_RPC_URL", "https://eth-mainnet.g.alchemy.com/v2/your-api-key"
            ),
            "arbitrum": os.getenv(
                "ARBITRUM_RPC_URL", "https://arb-mainnet.g.alchemy.com/v2/your-api-key"
            ),
            "polygon": os.getenv(
                "POLYGON_RPC_URL",
                "https://polygon-mainnet.g.alchemy.com/v2/your-api-key",
            ),
            "bsc": os.getenv("BSC_RPC_URL", "https://bsc-dataseed.binance.org/"),
        }
        self.railgun_api_url = os.getenv(
            "RAILGUN_API_URL", "https://api.railgun.org/v1"
        )

        # Try to load from config file if env vars not set
        config_path = Path.home() / ".railgun" / "config.json"
        if config_path.exists() and not self.api_key:
            try:
                with open(config_path, "r") as f:
                    config_data = json.load(f)
                    self.api_key = self.api_key or config_data.get("api_key")
                    self.wallet_password = self.wallet_password or config_data.get(
                        "wallet_password"
                    )
                    self.rpc_endpoints.update(config_data.get("rpc_endpoints", {}))
                    self.railgun_api_url = config_data.get(
                        "railgun_api_url", self.railgun_api_url
                    )
            except Exception as e:
                logger.warning(f"Failed to load config file: {e}")
