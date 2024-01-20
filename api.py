from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import DeclarativeMeta, declared_attr



database_url = " "
Base: DeclarativeMeta = declarative_base()
























