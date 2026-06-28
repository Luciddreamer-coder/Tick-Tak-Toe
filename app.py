import os
from flask import Flask , render_template , redirect , url_for

app = Flask(__name__)

game_state = {
    "xState" : [0 , 0 , 0,  0,  0,  0,  0,  0 , 0],
    "yState" : [0 , 0 , 0,  0,  0,  0,  0,  0 , 0],
    "turn" : 1,
    "winner_message" : None,
    "match_over" : False

}
def sum(a,b,c):
    return a + b + c


def checkWin(xState , yState):
    wins = [[0,1,2] , [3,4,5] , [6,7,8] , [0,3,6] ,[1,4,7] ,[2,5,8], [0,4,8] , [2,4,6]]
    for win in wins:
        if(sum(xState[win[0]] ,xState[win[1]] ,xState[win[2]]) == 3):
            return "X Won the match"
        if(sum(yState[win[0]] ,yState[win[1]] ,yState[win[2]]) == 3):
            return "O Won the match"
    if 0 not in [x + y for x, y in zip(xState, yState)]:
        return "It's a Tie!"
        
    return None

@app.route("/")
def Index():
    display_board =[]
    for i in range(9):
        if game_state["xState"][i] == 1:
            display_board.append("X")
        elif game_state["yState"][i] == 1:
            display_board.append("O")
        else:
            display_board.append("") # Empty string for styling empty squares
            
    return render_template('index.html', game=game_state, board=display_board)

@app.route('/move/<value>')
def make_move(value):
    value = int(value)
    if game_state["match_over"]:
        return  redirect(url_for('index'))
    if game_state["xState"][value] == 0 and game_state["yState"][value] == 0:
        if game_state["turn"] == 1:
            game_state["xState"][value] = 1
        else:
            game_state["yState"][value] = 1

        win_status = checkWin(game_state["xState"], game_state["yState"])
        if win_status is not None:
            game_state["winner_message"] = win_status
            game_state["match_over"] = True
        else:
            # Switch turn using your exact assignment: turn = 1 - turn
            game_state["turn"] = 1 - game_state["turn"]
            
    return redirect(url_for('Index'))

@app.route('/reset')
def reset():
    global game_state
    game_state = {
        "xState": [0, 0, 0, 0, 0, 0, 0, 0, 0],
        "yState": [0, 0, 0, 0, 0, 0, 0, 0, 0],
        "turn": 1,
        "winner_message": None,
        "match_over": False
    }
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=os.getenv('FLASK_DEBUG', False))