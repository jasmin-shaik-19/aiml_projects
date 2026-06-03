import java.util.Scanner;
class tictactoe
{
    // inside static method only static variables and static methods can be accessible so inside static main method we use static methods and board should be static 

    static char[][] board=new char[3][3];
    
    //----------if we declare board inside the method then other methods cannot be able to access it----

    public static void main(String a[])
    {
        Scanner sc = new Scanner(System.in);
        char currentplayer='x';
        boolean gameOver=false;
        initializeBoard();
        while(!gameOver)
        {
            printBoard();
            System.out.println("player "+currentplayer+"enter row and column ");
            int row=sc.nextInt();
            int col=sc.nextInt();

            //----------check if pposition is valid or not 

            if(row>=0 && row<3 && col>=0 && col<3 && board[row][col]=='-')
            {
                board[row][col]=currentplayer;
                if(checkwinner(currentplayer))
                {
                    printBoard();
                    System.out.println("player"+currentplayer+"wins");
                    gameOver=true;
                }
                else if(isBoardFull())
                {
                    printBoard();
                    System.out.println("its a draw");
                    gameOver=true;
                }

                //---------giving chance to other player ----------

                else
                {
                    currentplayer=(currentplayer=='x')?'o':'x';
                }
            }
            else
            {
                System.out.println("invalid move! try again");

            }
            

        }
        sc.close();

    }
    static void initializeBoard()
    {
        //---------------printing empty board --------------

        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                board[i][j]='-';
            }

        }   
    }
    static void printBoard()
    {
        //----------printing the board after updating the values-------------

        System.out.println("\nBoard:");
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                System.out.print(board[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println();
    }
    static boolean checkwinner(char player)
    {
        // -----------check rows------------

        for(int i=0;i<3;i++)
        {
            if(board[i][0]==player && board[i][1]==player && board[i][2]==player)
            {
                return true;
            }
        }

        // -------------------check columns---------------

        for(int i=0;i<3;i++)
        {
            if(board[0][i]==player && board[1][i]==player && board[2][i]==player)
            {
                return true;
            }
        }

        //--------------check diagonals------------------

        for(int i=0;i<3;i++)
        {
            if(board[0][0]==player && board[1][1]==player && board[2][2]==player)
            {
                return true;
            }
        }
        for(int i=0;i<3;i++)
        {
            if(board[0][2]==player && board[1][1]==player && board[2][0]==player)
            {
                return true;
            }
        }
        return false;
    }
    static boolean isBoardFull()
    {
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                if(board[i][j]=='-')
                {
                    return false;
                }
            }
        }
        return true;
    }

    
}