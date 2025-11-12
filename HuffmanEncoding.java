import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Node implements  Comparable<Node>{

    char ch ;
    int freq;
    Node left , right;

    public Node(char ch , int freq){
        this.ch = ch;
        this.freq = freq;
        this.left = this.right = null;
    }

    public Node( int freq , Node left ,Node right){
        this.freq = freq;
        this.left = left;
        this.right = right;
    }


    @Override
    public int compareTo(Node other){
        return Integer.compare(this.freq, other.freq);
    }
}

public class HuffmanEncoding{

    public static void generateCodes(Node root , String code , Map<Character , String > huffmanCode){
        if(root == null){
            return;
        }
        if(root.left == null && root.right == null){
            huffmanCode.put(root.ch, code.length() > 0 ? code : "0");
        }

        generateCodes(root.left, code + "0", huffmanCode);
        generateCodes(root.right, code + "1", huffmanCode);
    }

    public static void buildHuffmanTree(String text){
        //1.Frequqncy Counter
        Map<Character , Integer> freqMap = new HashMap<>();
        for(char ch : text.toCharArray()){
            freqMap.put(ch, freqMap.getOrDefault(ch, 0)+1);
        }

        //2.Priority Queue
        PriorityQueue<Node> pq = new PriorityQueue<>();
        for(var entry : freqMap.entrySet()){
            pq.add(new Node(entry.getKey(), entry.getValue()));
        }

        while(pq.size() > 1){
            Node left = pq.poll();
            Node right = pq.poll();

            Node mergedNode = new Node(left.freq + right.freq, left, right);
            pq.add(mergedNode);
        }
        Node root = pq.peek();

        Map<Character , String > huffmanCode = new HashMap<>();
        generateCodes(root, "", huffmanCode);

        System.out.println("\nHufffman Codes ");
        for(var entry : huffmanCode.entrySet()){
            System.out.println("'" + entry.getKey() + "':" + entry.getValue());
        }

        System.out.println("\nEncoded String");
        String encodedString = "";
        for(char ch : text.toCharArray()){
            encodedString += (huffmanCode.get(ch)+" ");
        }
        System.out.println(encodedString);
    }
    public static void main(String[] args) {
        String text = "Waigaonkar";
        buildHuffmanTree(text);
    }
}