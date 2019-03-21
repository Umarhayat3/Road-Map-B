from alembic import op
import sqlalchemy as sa
from alembic.templates.generic import*

sa.url = "sqlite:///test.db"
revision = '384ead9efdfd'

down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    pass

def downgrade():    pass
