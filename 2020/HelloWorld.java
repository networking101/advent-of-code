import java.util.*;

public class HelloWorld{

     public static void main(String []args){
        Scanner file = new Scanner(System.in);
        
        ArrayList<String> list = new ArrayList<String>();
        while(file.hasNext())
        {
            list.add(file.nextLine());
        }
        int j1 = 0;
        int j2 = 0;
        int j3 = 0;
        int j4 = 0;
        int j5 = 0;
        int trees1 = 0;
        int trees2 = 0;
        int trees3 = 0;
        int trees4 = 0;
        int trees5 = 0;
        for(int i = 0 ; i < list.size(); i++)
        {
            if(list.get(i).charAt(j1) == '#')
            {
                trees1++;
            }
            if(list.get(i).charAt(j2) == '#')
            {
                trees2++;
            }
            if(list.get(i).charAt(j3) == '#')
            {
                trees3++;
            }
            if(list.get(i).charAt(j4) == '#')
            {
                trees4++;
            }
            
            j1=j1+1;
            if(j1 >= list.get(i).length())
            {
                j1 = j1-list.get(i).length();
            }
            j2=j2+3;
            if(j2 >= list.get(i).length())
            {
                j2 = j2-list.get(i).length();
            }
            j3=j3+5;
            if(j3 >= list.get(i).length())
            {
                j3 = j3-list.get(i).length();
            }
            j4=j4+7;
            if(j4 >= list.get(i).length())
            {
                j4 = j4-list.get(i).length();
            }
        }
        for(int i = 0 ; i < list.size(); i=i+2)
        {
            if(list.get(i).charAt(j5) == '#')
            {
                trees5++;
            }
            j5 = j5 + 1;
            if(j5 >= list.get(i).length())
            {
                j5 = j5-list.get(i).length();
            }
        }
        System.out.println(trees1 + " " + trees2 + " " + trees3 + " " + trees4 + " " + trees5);
        System.out.println(trees1 * trees2 * trees3 * trees4 * trees5);
        //this doesn't actually work. Overflows int max value. Had to manually multiple them in google :/
        
     }
}
