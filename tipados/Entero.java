packages tipados;
import  java.util.Scanner;

public class Enter {
    Run|Debug
    public static void main(String[]args){
        int valor = -1;
        Scanner sc = new Scanner(System.in);
        String[] dias = {"Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"};
        while(valor<1 | valor>6){
            System.out.print("Ingrese un entero: ");
            valor = sc.nextInt();
        }

       
        System.out.println(dias[valor]);
        /*
        for(int i = 0; i < valor; i++){
            System.out.print(i);
        }

        switch (valor) {
            case 1:
                System.out.println("domingo");                
                break;
            case 2:
                System.out.println("Lunes");                
                break;
            case 3:
                System.out.println("Martes");                
                break;
            case 4:
                System.out.println("Miercoles");                
                break;
            case 5:
                System.out.println("Jueves");                
                break;                
            default:
                System.out.
                break;
        }*/

    }
}