import java.util.Random;

public class GenerateGrades {

	public static void main(String[] args) {
		double totalGrade = 50;
		double maxGrade = totalGrade / 4;
		double minGrade = maxGrade - 0.0000001;
				
		Random rand = new Random();
		double grade[] = new double[4];
		double runningCount = 0;
		double actualTotal = 0;
		
		for(int i=0; i < grade.length-1; i++) {
			grade[i] = minGrade + (maxGrade - minGrade) * rand.nextDouble();
			runningCount += grade[i];
		}
		grade[3] = totalGrade - runningCount;
		
		for(int i=0; i < grade.length; i++) {
			System.out.println("Grade " + (i+1) + ": " + grade[i]);
			actualTotal += grade[i];
		}
		
		System.out.println("Total: " + actualTotal);
	}
}
