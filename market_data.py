from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

import threading
import time

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = []

    def historicalData(self, bar):
        self.data.append([bar.date, bar.open, bar.high, bar.low, bar.close])

