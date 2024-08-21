import javax.swing.*;
import java.awt.event.*;
import java.awt.* ;
public class rules extends JFrame implements ActionListener
{
	String name;
	JButton proceed;
	rules(String name)
	{
		this.name=name;
		setSize(1400,700) ;
		setVisible(true) ;
		setLocation(75,100) ;
		setLayout(null);
		setDefaultCloseOperation(EXIT_ON_CLOSE) ;
		getContentPane().setBackground(Color.WHITE) ;
		
		JLabel heading1=new JLabel("CODEMASTERY");
		heading1.setBounds(100,50,500,60);
		add(heading1);
		heading1.setFont(new Font("Viner Hand ITC",Font.BOLD,45));
		heading1.setForeground(Color.BLUE);
		
		JLabel heading2=new JLabel("Welcome " + name);
		heading2.setBounds(100,130,500,60);
		add(heading2);
		heading2.setFont(new Font("Times New Roman",Font.BOLD,30));
		
		JLabel heading3=new JLabel("RULES :");
		heading3.setBounds(100,200,500,60);
		add(heading3);
		heading3.setFont(new Font("Times New Roman",Font.BOLD,25));
		
		JLabel heading4=new JLabel();
		heading4.setBounds(100,270,800,280);
		add(heading4);
		heading4.setFont(new Font("Times New Roman",Font.PLAIN,25));
		heading4.setText
		(
			"<html>"+
			"1. This is a multiple choice type test."+"<br></br>"+
			"2. Each question is timed. Quiz will jump to next question if time is over."+"<br></br>"+
			"3. The test will auto-submit when the time duration is over."+"<br></br>"+
			"4. You are not allowed to use any electronic device to search for answers of the test."+"<br></br>"+
			"5. There is only one correct answer to every question."+"<br></br>"+
			"6. The test will start when 'Proceed' button is clicked."+"<br></br>"+"<br></br>"+
			"Good Luck !"+"<br></br>"+
			"</html>"
		);
		
		proceed=new JButton("Proceed");
		proceed.setBounds(650,550,100,30);
		proceed.setBackground(Color.BLUE);
		proceed.setForeground(Color.WHITE);
		proceed.addActionListener(this);
		add(proceed);
	}
	public void actionPerformed(ActionEvent e)
	{
		if(e.getSource()==proceed)
		{
			setVisible(false);
			new quiz(name);
		}
	}
	public static void main(String args[])
	{
		new rules("User");
	}
}
