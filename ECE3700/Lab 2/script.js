function Gameboard() {
    this.board = [
        ['','',''],
        ['','',''],
        ['','','']
    ]
    this.moves = 0

    this.printBoard = () => {
        console.log(this.board[0][0], this.board[0][1], this.board[0][2]);
        console.log(this.board[1][0], this.board[1][1], this.board[1][2]);
        console.log(this.board[2][0], this.board[2][1], this.board[2][2]);
    }

    this.updateBoard = (row, col, player) => {
        if (this.board[row][col] === '') {
            this.board[row][col] = player;
            this.moves++;
        }
    }

    this.checkWinner = () => {
        for (let i = 0; i < 3; i++) {
            if (this.board[i][0] === this.board[i][1] && this.board[i][1] === this.board[i][2] && this.board[i][0] !== '') {
                return this.board[i][0];
            }
            if (this.board[0][i] === this.board[1][i] && this.board[1][i] === this.board[2][i] && this.board[0][i] !== '') {
                return this.board[0][i];
            }
        }
        if (this.board[0][0] === this.board[1][1] && this.board[1][1] === this.board[2][2] && this.board[0][0] !== '') {
            return this.board[0][0];
        }
        if (this.board[0][2] === this.board[1][1] && this.board[1][1] === this.board[2][0] && this.board[0][2] !== '') {
            return this.board[0][2];
        }
        if (this.moves === 9) {
            return 'Tie';
        }
        return '';
    }

    this.updateDOM = () => {
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                const cell = document.getElementById(`cell-${i}${j}`);
                cell.innerHTML = this.board[i][j];
            }
        }
    }

    this.reset = () => {
        this.board = [
            ['','',''],
            ['','',''],
            ['','','']
        ]
        this.moves = 0;
    }

    this.displayWinner = (winner) => {
        const winnerDisplay = document.getElementById('winner-display');
        winnerDisplay.innerHTML = `${winner}`;
    }
}

const resetGame = () => {
    const resetButton = document.createElement('button');
    resetButton.innerHTML = 'Reset';
    resetButton.id = 'reset-button';
    document.body.appendChild(resetButton);
    resetButton.addEventListener('click', () => {
        game.reset();
        game.updateDOM();
        const winnerDisplay = document.getElementById('winner-display');
        winnerDisplay.innerHTML = '';
    });
}


const game = new Gameboard();
const cells = document.querySelectorAll('.cell');
let player = 'X';
cells.forEach(cell => {
    cell.addEventListener('click', () => {
        let win = game.checkWinner();
        if (win === "")
        {
            const row = parseInt(cell.id[5]);
            const col = parseInt(cell.id[6]);
            game.updateBoard(row, col, player);
            player = player === 'X' ? 'O' : 'X';
            win = game.checkWinner();
            console.log(row, col);
            game.printBoard();
            game.updateDOM();
        }
        if (win === 'X') {
            game.displayWinner('X Wins!');
            resetGame();
        } else if (win === 'O') {
            game.displayWinner('O Wins!');
            resetGame();            
        } else if (win === 'Tie') {
            game.displayWinner('It\'s a tie!');
            resetGame();
        }
    });
});

