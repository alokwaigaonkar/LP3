
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

class Item {
    int value , weight;
    double ratio;

    public Item(int value , int weight) {
        this.value = value;
        this.weight = weight;
        this.ratio = (double) (value/weight);
    }
}



public class FractionalKnapSack {
    public static double getMaxValue(int [] value , int [] weight , int capacity){
        List<Item> items = new ArrayList<>();
        for(int i =0;i<value.length;i++){
            items.add(new Item(value[i], weight[i]));
        }
        Collections.sort(items,(a,b)->Double.compare(b.ratio, a.ratio));

        double totalValue = 0;
        int currentWeight = 0;

        for(Item item : items){
            if(currentWeight+item.weight <= capacity){
                totalValue +=item.value;
                currentWeight+=item.weight;
            }else{
                int remainingWeight = capacity - currentWeight;
                totalValue += item.ratio * remainingWeight;
                break;
            }
        }
        return totalValue;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input section
        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        int[] value = new int[n];
        int[] weight = new int[n];

        System.out.println("Enter value and weight of each item:");
        for (int i = 0; i < n; i++) {
            System.out.print("Item " + (i + 1) + " - Value: ");
            value[i] = sc.nextInt();
            System.out.print("Item " + (i + 1) + " - Weight: ");
            weight[i] = sc.nextInt();
        }

        System.out.print("Enter knapsack capacity: ");
        int capacity = sc.nextInt();

        double maxValue = getMaxValue(value, weight, capacity);
        System.out.println("\nMaximum value in Knapsack = " + maxValue);

        sc.close();
    }
}
