import shutil
import os
from datetime import datetime

DATABASE = "app/database/database.db"

BACKUP_FOLDER = "app/database/backups"

os.makedirs(BACKUP_FOLDER, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

backup_file = os.path.join(
    BACKUP_FOLDER,
    f"database_backup_{timestamp}.db"
)

shutil.copy2(DATABASE, backup_file)

print("="*50)
print("DATABASE BACKUP CREATED")
print("="*50)
print("Backup File :", backup_file)