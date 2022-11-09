# codewars-unfollow
Unfollow all of your allies on Codewars

# How to use
1. Clone this repository
```git
git clone https://github.com/ngntrgduc/codewars-unfollow.git
```
2. Open the folder you have just cloned. Then create the `.env` file with the structure:
```
USER_NAME = <Your codewars username>
MAIL = <Your email>
PASSWORD = <Your password>
```
3. Open the terminal in that folder and install all dependencies:
```python
pip install -r requirements.txt
```
4. Run the script
```python
python main.py
```
# Note
- I use selenium with Microsoft Edge. If you want to use another browser, please check out [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager).
- There may be slow because needs 4 seconds to remove 1 following. You can delete `sleep` command to make it faster. But you may not unfollow some users, and the codewars site may block you (I tried and it block me 3 - 4 times).
- When the following is less than 15, you should remove them by yourself. (Sorry for that :<)