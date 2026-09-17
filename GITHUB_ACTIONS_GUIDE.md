# GitHub Actions CI/CD Guide

Complete guide to the GitHub Actions workflows for the Amazon Mobile Scraper project.

---

## Overview

This project includes 4 automated GitHub Actions workflows:

1. **Tests & Setup Verification** (`tests.yml`)
2. **Automated Web Scraping** (`scrape.yml`)
3. **Build & Release** (`build-release.yml`)
4. **Deploy & Monitor** (`deploy.yml`)

---

## 1. Tests & Setup Verification Workflow

**File**: `.github/workflows/tests.yml`

### What it does:
- Tests on multiple OS: Ubuntu, Windows, macOS
- Tests on multiple Python versions: 3.8, 3.9, 3.10, 3.11, 3.12
- Verifies all dependencies
- Runs code quality checks (Flake8, Pylint)
- Performs security scanning (Bandit, Safety)

### When it runs:
- On every push to master, main, or develop branches
- On every pull request
- Daily at 2 AM UTC (scheduled)

### Status badges you can add to README:
```markdown
![Tests](https://github.com/DataSpoof/amazon-mobile-scraper/workflows/Tests%20&%20Setup%20Verification/badge.svg)
```

### View results:
1. Go to your repo
2. Click "Actions" tab
3. Select "Tests & Setup Verification"
4. View latest run

---

## 2. Automated Web Scraping Workflow

**File**: `.github/workflows/scrape.yml`

### What it does:
- Installs Chrome and ChromeDriver
- Runs the Amazon mobile scraper
- Uploads results as artifacts
- Commits changes back to repository
- Creates issues on failure

### When it runs:
- Daily at 3 AM UTC (scheduled)
- Manually via GitHub Actions tab (workflow_dispatch)

### How to trigger manually:
1. Go to "Actions" tab
2. Select "Automated Web Scraping"
3. Click "Run workflow"
4. Wait for completion

### Results:
- `mobile_results.json` - Main results
- `mobile_results.csv` - CSV format
- `mobile_results_simple.json` - Simple format

### Artifacts retention:
- Results kept for 30 days
- Accessible from workflow run page

### Auto-commit feature:
- Results automatically committed to repo
- Commit message: `chore: update scraping results - DATE TIME`
- Only commits if results changed

---

## 3. Build & Release Workflow

**File**: `.github/workflows/build-release.yml`

### What it does:
- Runs tests before building
- Creates distribution packages
- Generates tar.gz and zip archives
- Creates GitHub releases
- Uploads release assets

### When it runs:
- When you push tags starting with `v` (e.g., `v1.0.0`)
- Manually via workflow_dispatch

### How to create a release:
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### Release assets created:
- `amazon-mobile-scraper.tar.gz`
- `amazon-mobile-scraper.zip`
- `mobile_results.json`
- `mobile_results.csv`

### Access releases:
1. Go to repository
2. Click "Releases" on right sidebar
3. View available versions

---

## 4. Deploy & Monitor Workflow

**File**: `.github/workflows/deploy.yml`

### What it does:
- Deploys application to production
- Runs health checks
- Creates deployment reports
- Automatically rolls back on failure
- Creates issues for failed deployments

### When it runs:
- On push to master/main branches
- Daily at 1 AM UTC
- Manually via workflow_dispatch

### Production environment:
- Configured in GitHub repository settings
- Can add approval requirements
- Tracks deployment history

### Health checks:
- Verifies setup
- Runs all tests
- Reports status

### Rollback mechanism:
- Automatically creates issue on failure
- Labels it as "deployment" and "critical"
- Manual rollback can be performed

---

## Workflow Features

### ✅ Features Included

#### Testing
- [x] Multi-OS testing (Ubuntu, Windows, macOS)
- [x] Multi-Python version support
- [x] Dependency verification
- [x] Code quality checks (Flake8, Pylint)
- [x] Security scanning (Bandit, Safety)

#### Scraping
- [x] Automated daily scraping
- [x] Results upload to artifacts
- [x] Auto-commit to repository
- [x] Failure notifications
- [x] Manual trigger option

#### Build & Release
- [x] Automated testing before build
- [x] Package creation (tar.gz, zip)
- [x] GitHub release creation
- [x] Asset uploads
- [x] Release notes generation

#### Deployment
- [x] Production environment config
- [x] Health checks
- [x] Deployment reports
- [x] Automatic rollback
- [x] Failure notifications

---

## Configuration

### Environment Variables
You can set environment variables in `.github/workflows/` files:

```yaml
env:
  SEARCH_QUERY: "mobile under 100000"
  PRICE_LIMIT: 100000
```

### Secrets
To use sensitive data (API keys, tokens):

1. Go to repository Settings
2. Click "Secrets and variables" → "Actions"
3. Add new secret
4. Use in workflow: `${{ secrets.SECRET_NAME }}`

### Matrix Strategy
Tests run on all combinations:
- OS: ubuntu-latest, windows-latest, macos-latest
- Python: 3.8, 3.9, 3.10, 3.11, 3.12

---

## Viewing Results

### GitHub Actions Dashboard
1. Go to your repository
2. Click "Actions" tab
3. Select workflow name
4. View run details

### Artifacts
1. Open workflow run
2. Scroll to "Artifacts" section
3. Download artifact zip

### Logs
1. Click on job name
2. View detailed step logs
3. Check for errors/warnings

---

## Scheduling

### Cron Syntax
```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 6)
│ │ │ │ │
│ │ │ │ │
0 2 * * *
```

### Current Schedules
- **Tests**: Daily 2 AM UTC
- **Scraping**: Daily 3 AM UTC
- **Deployment**: Daily 1 AM UTC

### Modify schedules
Edit `.github/workflows/` files and change cron expression.

---

## Best Practices

### 1. Security
- Use GitHub Secrets for sensitive data
- Never commit credentials
- Use environment-specific configurations
- Review logs for exposed data

### 2. Performance
- Cache dependencies when possible
- Use matrix strategy efficiently
- Clean up old artifacts
- Optimize workflow triggers

### 3. Reliability
- Add retry logic for flaky tests
- Use continue-on-error for non-critical steps
- Monitor workflow history
- Set up notifications

### 4. Documentation
- Comment complex workflow steps
- Document custom variables
- Keep workflow README updated
- Share results with team

---

## Troubleshooting

### Workflow not triggering
- Check branch filters
- Verify cron syntax
- Check GitHub Actions is enabled
- Review workflow status page

### Tests failing
- Check Python version compatibility
- Verify dependencies installed
- Review test logs
- Run locally first

### Build failures
- Check system requirements
- Verify file permissions
- Review error messages
- Check artifact size limits

### Deployment issues
- Verify environment configuration
- Check health check results
- Review deployment logs
- Check production status

---

## Common Errors & Solutions

### Error: "Could not find Chrome"
**Solution**: Workflow already installs Chrome in Ubuntu. For other OS, add:
```yaml
- name: Setup Chrome
  uses: browser-actions/setup-chrome@latest
```

### Error: "Permission denied"
**Solution**: Check file permissions and git credentials:
```yaml
- name: Configure git
  run: |
    git config --local user.email "action@github.com"
    git config --local user.name "GitHub Action"
```

### Error: "Artifact not found"
**Solution**: Verify paths in upload-artifact action match actual files

---

## Advanced Usage

### Custom notifications
Add to workflow:
```yaml
- name: Notify Slack
  uses: slackapi/slack-github-action@v1
  with:
    webhook-url: ${{ secrets.SLACK_WEBHOOK }}
```

### Database integration
Add to scraping workflow:
```yaml
- name: Upload to database
  run: |
    python upload_to_db.py --results mobile_results.json
  env:
    DB_CONNECTION: ${{ secrets.DB_CONNECTION }}
```

### Email reports
```yaml
- name: Send email report
  uses: davisre/action-mailer@master
  with:
    server_address: ${{ secrets.MAIL_SERVER }}
    to: ${{ secrets.MAIL_TO }}
    subject: Scraping Results
```

---

## Monitoring & Analytics

### View workflow statistics
1. Go to "Insights" → "Workflows"
2. View success/failure rates
3. Check execution times
4. Analyze resource usage

### Set up notifications
1. Repository Settings → Notifications
2. Enable workflow notifications
3. Choose notification method (email, web)

---

## Disabling workflows

To temporarily disable a workflow:
1. Go to Actions tab
2. Click workflow name
3. Click "..." menu
4. Select "Disable workflow"

To re-enable:
1. Go to Actions tab
2. Click workflow name
3. Click "..." menu
4. Select "Enable workflow"

---

## Summary

| Workflow | Trigger | Frequency | Purpose |
|----------|---------|-----------|---------|
| Tests | Push/PR | Every push | Verify setup & quality |
| Scraping | Schedule | Daily 3 AM | Automated data collection |
| Build | Tags | On tag | Create releases |
| Deploy | Push | On merge | Production deployment |

---

## Next Steps

1. **Monitor workflows**: Check Actions tab after each push
2. **Review logs**: Investigate any failures
3. **Customize schedules**: Adjust times as needed
4. **Add notifications**: Set up Slack/email alerts
5. **Scale up**: Add more workflows as needed

---

**GitHub Actions is now configured! Your project has full CI/CD automation! 🚀**
