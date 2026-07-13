"""Database connection and session management."""

from contextlib import contextmanager
from typing import Generator

import psycopg2
from psycopg2.extras import RealDictConnection

from .config import DatabaseConfig


class Database:
    """PostgreSQL database connection manager."""
    
    def __init__(self, config: DatabaseConfig):
        self.config = config
        self._connection = None
    
    def connect(self) -> None:
        """Establish database connection."""
        self._connection = psycopg2.connect(
            host=self.config.host,
            port=self.config.port,
            database=self.config.name,
            user=self.config.user,
            password=self.config.password,
        )
    
    def disconnect(self) -> None:
        """Close database connection."""
        if self._connection:
            self._connection.close()
            self._connection = None
    
    @contextmanager
    def cursor(self) -> Generator:
        """Get database cursor as context manager."""
        if not self._connection:
            self.connect()
        
        cursor = self._connection.cursor(cursor_factory=RealDictConnection)
        try:
            yield cursor
            self._connection.commit()
        except Exception:
            self._connection.rollback()
            raise
        finally:
            cursor.close()
    
    def execute(self, query: str, params: tuple = None) -> list:
        """Execute query and return results."""
        with self.cursor() as cur:
            cur.execute(query, params)
            if cur.description:
                return cur.fetchall()
            return []
    
    def execute_many(self, query: str, params_list: list) -> None:
        """Execute query with multiple parameter sets."""
        with self.cursor() as cur:
            cur.executemany(query, params_list)
