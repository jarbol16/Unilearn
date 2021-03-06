"""empty message

Revision ID: 4767bd9dc667
Revises: None
Create Date: 2015-03-23 17:14:13.473175

"""

# revision identifiers, used by Alembic.
revision = '4767bd9dc667'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('topic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('icon', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=300), nullable=True),
    sa.Column('password', sa.String(length=300), nullable=True),
    sa.Column('photo', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('username'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.Column('statement', sa.Text(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('msm_question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clasification_question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('completation_question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pairing_question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state', sa.Boolean(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('msu_question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('msu_question')
    op.drop_table('answer')
    op.drop_table('pairing_question')
    op.drop_table('completation_question')
    op.drop_table('clasification_question')
    op.drop_table('msm_question')
    op.drop_table('question')
    op.drop_table('user')
    op.drop_table('topic')
    ### end Alembic commands ###
