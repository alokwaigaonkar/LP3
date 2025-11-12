public class Queen {

    static int  N;
    public static void solveQueens(int [][] board, int row){
        if(row >= N){
            printBoard(board);
            return ;
        }

        for(int col =0;col<N;col++){
            if(isSafe( board ,  row ,  col)){
                board[row][col] =1;
                
                solveQueens(board, row+1);
                
                board[row][col] =0;
            }
        }
        
    }

    public static boolean isSafe(int [] [] board , int row , int col){
        //check upper rows of this column
        for(int i =0;i<row ;i++){
            if(board[i][col] == 1){
                return false;
            }
        }

        //check upper left daigonal
        for(int i =row-1,j=col-1;i>=0 && j>=0;i--,j--){
            if(board[i][j] ==1){
                return false;
            }
        }
        //check upper right daigonal

        for(int i =row-1,j=col+1;i>=0 && j<N;i--,j++){
            if(board[i][j] == 1){
                return false;
            }
        }
        return true;
    }
    public static void  printBoard(int [] [] board){
        for(int i =0;i<N;i++){
            for(int j=0;j<N;j++){
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        N=8;
        int [][] board = new int[N][N];
        board[0][0] =1 ;
        solveQueens(board, 1);
    }
}
