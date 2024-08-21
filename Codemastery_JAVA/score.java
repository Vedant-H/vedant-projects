import javax.swing.*;
import java.awt.event.*;
import java.awt.* ;
public class score extends JFrame implements ActionListener
{
	JButton submit;
	score(String name,int score)
	{
		setSize(1400,700) ;
		setVisible(true) ;
		setLocation(75,100) ;
		setLayout(null);
		setDefaultCloseOperation(EXIT_ON_CLOSE) ;
		getContentPane().setBackground(Color.WHITE) ;
		
		ImageIcon i1=new ImageIcon("score2.JPEG") ;
		JLabel image=new JLabel(i1) ;
		image.setBounds(300,0,800,300) ;
		add(image) ;
		
		JLabel heading=new JLabel("Thank You " + name + " for playing CodeMastery !");
		heading.setBounds(450,400,500,30);
		heading.setFont(new Font("Tahoma",Font.BOLD,20));
		add(heading);
		
		JLabel marks=new JLabel("Score : " + score + "/100");
		marks.setBounds(450,450,500,30);
		marks.setFont(new Font("Tahoma",Font.BOLD,20));
		add(marks);
		
		submit=new JButton("Play Again");
		submit.setBounds(450,550,200,40);
		submit.setBackground(Color.BLUE);
		submit.setForeground(Color.WHITE);
		submit.setFont(new Font("Tahoma",Font.BOLD,20));
		submit.addActionListener(this);
		add(submit);
	}
	
	public void actionPerformed(ActionEvent aee)
	{
		if(aee.getSource()==submit)
		{
			setVisible(false);
			new tp();
		}
	}
	
	public static void main(String args[])
	{
		new score("User",0);
	}
}
