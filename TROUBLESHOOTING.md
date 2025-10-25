# Troubleshooting Guide

## Common Installation Issues

### Issue: "No matching distribution found for scipy"

**Cause:** Version incompatibility with your Python version.

**Solution:**
```bash
# Update pip first
pip install --upgrade pip

# Install with compatible versions
pip install -r requirements.txt
```

If still failing, install packages individually:
```bash
pip install numpy
pip install scipy
pip install pandas
pip install matplotlib
pip install flask
pip install flask-cors
```

### Issue: "python: command not found"

**Cause:** Python is installed as `python3` on your system.

**Solution:** Use `python3` instead of `python`:
```bash
python3 -m venv venv
python3 app.py
```

### Issue: "Permission denied" when running setup.sh

**Cause:** Script doesn't have execute permissions.

**Solution:**
```bash
chmod +x setup.sh
./setup.sh
```

### Issue: "venv/Scripts/activate: No such file or directory"

**Cause:** You're using Linux/Mac commands on Windows or vice versa.

**Solution:**
- **Windows:** `venv\Scripts\activate`
- **Linux/Mac:** `source venv/bin/activate`

## Common Runtime Issues

### Issue: "ECONNREFUSED" or "Network Error" in frontend

**Cause:** Backend server is not running.

**Solution:**
1. Start the backend server first:
   ```bash
   cd backend/api
   python3 app.py
   ```
2. Verify it's running at http://localhost:5000/api/health
3. Then start the frontend

### Issue: "Address already in use" on port 5000

**Cause:** Another application is using port 5000.

**Solution 1:** Stop the other application

**Solution 2:** Change the backend port
- Edit `backend/api/app.py`, line with `app.run()`:
  ```python
  app.run(debug=True, host='0.0.0.0', port=5001)  # Changed to 5001
  ```
- Edit `next.config.js`:
  ```javascript
  destination: 'http://localhost:5001/api/:path*',  // Changed to 5001
  ```

### Issue: "Address already in use" on port 3000

**Cause:** Another application is using port 3000.

**Solution:** Run Next.js on a different port:
```bash
npm run dev -- -p 3001
```
Then open http://localhost:3001

### Issue: CORS errors

**Symptoms:** Browser console shows "CORS policy" errors

**Solution:**
1. Verify both servers are running
2. Check that flask-cors is installed: `pip list | grep flask-cors`
3. Restart the backend server

### Issue: Charts/visualizations not appearing

**Cause:** Matplotlib backend issue or missing dependencies.

**Solution:**
```bash
# Install additional dependencies
pip install pillow
```

If on Linux:
```bash
sudo apt-get install python3-tk
```

### Issue: "Module not found" errors in Python

**Cause:** Virtual environment not activated or dependencies not installed.

**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows

# Reinstall dependencies
cd backend
pip install -r requirements.txt
```

### Issue: TypeScript errors in frontend

**Cause:** Dependencies not installed.

**Solution:**
```bash
# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

### Issue: "Cannot find module '@/lib/api'" in Next.js

**Cause:** TypeScript path mapping not recognized.

**Solution:**
1. Verify `tsconfig.json` has the paths configuration
2. Restart the Next.js dev server
3. If using an IDE, restart it

## Platform-Specific Issues

### Windows-Specific

**Issue:** Scripts fail with line ending errors

**Solution:**
```bash
git config --global core.autocrlf true
```

**Issue:** Permission errors creating virtual environment

**Solution:** Run Command Prompt or PowerShell as Administrator

### Linux/Mac-Specific

**Issue:** pip: command not found

**Solution:**
```bash
python3 -m ensurepip
# OR
sudo apt-get install python3-pip  # Ubuntu/Debian
brew install python3              # macOS
```

**Issue:** Port binding permission error (ports < 1024)

**Solution:** Use ports >= 1024 (default 5000 and 3000 are fine)

## Verification Steps

### Verify Backend

1. Activate virtual environment
2. Check dependencies:
   ```bash
   pip list
   ```
   Should show: flask, flask-cors, numpy, scipy, pandas, matplotlib

3. Test the API:
   ```bash
   cd backend/api
   python3 app.py
   ```
   You should see: "Running on http://127.0.0.1:5000"

4. Test endpoint:
   ```bash
   curl http://localhost:5000/api/health
   ```
   Should return: `{"status":"healthy","message":"Options Pricing API is running"}`

### Verify Frontend

1. Check Node.js and npm:
   ```bash
   node --version  # Should be >= 18.0
   npm --version
   ```

2. Check dependencies installed:
   ```bash
   ls node_modules
   ```
   Should see: next, react, axios, etc.

3. Start dev server:
   ```bash
   npm run dev
   ```
   Should see: "ready - started server on 0.0.0.0:3000"

## Getting Help

If you've tried all the above and still have issues:

1. **Check the Error Message:** Most error messages contain helpful information
2. **Check Both Terminals:** Look for errors in both backend and frontend terminals
3. **Verify Versions:**
   - Python 3.8+: `python3 --version`
   - Node.js 18+: `node --version`
4. **Clean Install:**
   ```bash
   # Backend
   rm -rf venv
   python3 -m venv venv
   source venv/bin/activate
   cd backend
   pip install -r requirements.txt

   # Frontend
   rm -rf node_modules package-lock.json .next
   npm install
   ```

5. **Create an Issue:** Open an issue on GitHub with:
   - Your operating system
   - Python version
   - Node.js version
   - Complete error message
   - Steps to reproduce

## Quick Diagnostic

Run this to check your environment:

```bash
echo "Python version:"
python3 --version

echo -e "\nNode.js version:"
node --version

echo -e "\nnpm version:"
npm --version

echo -e "\nPip packages:"
pip list | grep -E "numpy|scipy|pandas|matplotlib|flask"

echo -e "\nNode modules:"
ls node_modules | grep -E "next|react|axios"
```

Everything working? Start the servers:

**Terminal 1:**
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
cd backend/api
python3 app.py
```

**Terminal 2:**
```bash
npm run dev
```

Open http://localhost:3000 and enjoy! 🎉
