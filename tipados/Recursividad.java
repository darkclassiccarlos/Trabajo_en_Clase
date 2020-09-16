package tipados;

public class Recursividad{
    Run|Debug
    public static void main(String[] args){
        System.out.println(producto(5,3))
        System.out.println(productoIterativo(5,3));

    }
    public int producto (int n, int m){
        if(n==1){
            return n;
        }
        return producto(n, m-1)+n;
    }

    public static int productoIterativo(int n, int m){
        int valor = 0;
        for(int i = 0; i <m; i++)
            valor += n;
    
            return valor;
            }
}