# Colab info

```python
import logging

# Set the logging level to INFO
logging.basicConfig(level=logging.INFO, force=True)
logging.info("This is an info message")  
```

# auto download file

```python
from google.colab import files
files.download('judgments_azure.json')	
```

