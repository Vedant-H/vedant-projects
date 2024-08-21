import javax.swing.*;
import java.awt.event.*;
import java.awt.* ;
public class tp extends JFrame implements ActionListener{
	JButton rules;
	JTextField tfname;
	tp()
	{
		setSize(1400,700) ;
		setVisible(true) ;
		setLocation(75,100) ;
		setLayout(null);
		setDefaultCloseOperation(EXIT_ON_CLOSE) ;
		
		getContentPane().setBackground(Color.WHITE) ;
		
		ImageIcon i1=new ImageIcon("quiztime1.JPEG") ;
		JLabel image=new JLabel(i1) ;
		image.setBounds(0,0,600,700) ;
		add(image) ;
		
		JLabel heading=new JLabel("CODEMASTERY");
		heading.setBounds(750,150,500,60);
		add(heading);
		heading.setFont(new Font("Viner Hand ITC",Font.BOLD,60));
		heading.setForeground(Color.BLUE);
		
		JLabel name=new JLabel("Enter Name :");
		name.setBounds(750,300,150,30);
		name.setFont(new Font("Times New Roman",Font.BOLD,25));
		name.setForeground(Color.BLUE);
		add(name);
		
		tfname=new JTextField();
		tfname.setBounds(900,300,350,30);
		add(tfname);
		tfname.setFont(new Font("Mongolian Baiti",Font.BOLD,25));
		
		rules=new JButton("Proceed to Rules >>");
		rules.setBounds(900,400,200,30);
		rules.setBackground(Color.BLUE);
		rules.setForeground(Color.WHITE);
		rules.addActionListener(this);
		add(rules);
	}
	
	public void actionPerformed(ActionEvent e)
	{
		if(e.getSource() ==rules)
		{
			String name=tfname.getText();
			setVisible(false);
			new rules(name);
		}
	}
	
	public static void main(String args[])
	{
		new tp() ;
	}
}
