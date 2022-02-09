# Generated by Django 2.2 on 2022-02-09 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0042_auto_20211217_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='distribution_type',
            field=models.CharField(choices=[('FLAG_PAPER', 'FLAG_PAPER'), ('PAPER_UPVOTED', 'PAPER_UPVOTED'), ('CREATE_BULLET_POINT', 'CREATE_BULLET_POINT'), ('BULLET_POINT_FLAGGED', 'BULLET_POINT_FLAGGED'), ('BULLET_POINT_UPVOTED', 'BULLET_POINT_UPVOTED'), ('BULLET_POINT_DOWNVOTED', 'BULLET_POINT_DOWNVOTED'), ('COMMENT_CENSORED', 'COMMENT_CENSORED'), ('COMMENT_FLAGGED', 'COMMENT_FLAGGED'), ('COMMENT_UPVOTED', 'COMMENT_UPVOTED'), ('COMMENT_DOWNVOTED', 'COMMENT_DOWNVOTED'), ('REPLY_CENSORED', 'REPLY_CENSORED'), ('REPLY_FLAGGED', 'REPLY_FLAGGED'), ('REPLY_UPVOTED', 'REPLY_UPVOTED'), ('REPLY_DOWNVOTED', 'REPLY_DOWNVOTED'), ('THREAD_CENSORED', 'THREAD_CENSORED'), ('THREAD_FLAGGED', 'THREAD_FLAGGED'), ('THREAD_UPVOTED', 'THREAD_UPVOTED'), ('THREAD_DOWNVOTED', 'THREAD_DOWNVOTED'), ('CREATE_SUMMARY', 'CREATE_SUMMARY'), ('SUMMARY_UPVOTED', 'SUMMARY_UPVOTED'), ('SUMMARY_DOWNVOTED', 'SUMMARY_DOWNVOTED'), ('REWARD', 'REWARD'), ('PURCHASE', 'PURCHASE'), ('REFERRAL', 'REFERRAL'), ('EDITOR_COMPENSATION', 'EDITOR_COMPENSATION')], max_length=255),
        ),
    ]
