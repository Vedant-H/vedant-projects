import express from "express";
import bodyParser from "body-parser";
import pg from "pg";
import axios from "axios";

const app=express();
const port=3000;

const db=new pg.Client({
    user: "postgres",
    host: "localhost",
    database: "project",
    password: "Root@1234",
    port: 5432,
  });

db.connect();


app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());

app.get("/", async (req,res)=>{
const result=await db.query("SELECT * FROM books order by id asc; ");
    res.render("index.ejs",{
        item:result.rows
    });
})

app.post("/filter", async (req,res)=>{
    const id=req.body.type;
    if(id=="1"){
        const result=await db.query("SELECT * FROM books ORDER BY rate DESC");
            res.render("index.ejs",{
                item:result.rows
            }); 
    }
    else{
        const result=await db.query("SELECT * FROM books ORDER BY id DESC");
        res.render("index.ejs",{
            item:result.rows
        });  
    }

});

app.post("/add", async (req,res)=>{
    console.log(req.body,req.params);
    
    try {const book_name=req.body.bname;
    const isbn=req.body.isbn;
    const author=req.body.author;
    const date=new Date();
    const book_data=await axios.get(`https://covers.openlibrary.org/b/isbn/${isbn}.json`);
    console.log(book_data);
    const book_url=book_data.data.source_url;
    const rate=req.body.rate;
     await db.query("INSERT INTO books (name,isbn,author,date,url,rate) VALUES ($1,$2,$3,$4,$5,$6)",[book_name,isbn,author,date,book_url,rate]);
     res.redirect("/");
    }
    catch(err){
        console.log(err);
        const result= await db.query("SELECT * FROM books order by id asc; ");
        res.render("index.ejs",{item:result.rows ,merror:{msg:"Data not found "}})
        return ;
    }
    
})

app.post("/delete", async (req,res)=>{
    const isbn=req.body.deleteItemISBN;
    await db.query("DELETE FROM details WHERE book_isbn=$1",[isbn]);
    await db.query("DELETE FROM books WHERE isbn=$1",[isbn]);
    res.redirect("/");
})

async function getData(isbn) {
    return await db.query("select * from books join details on book_isbn = books.isbn where books.isbn=$1",[isbn]);
}

app.post("/about/:id", async(req,res)=>{

    const isbn=req.params.id;
    const summary=req.body.summary
    const data=req.body.data;
    const dateChange=new Date();
   
    await db.query("UPDATE details SET summary=$1 ,data=$2 ,datechange= $3 WHERE book_isbn=$4 ",[summary,data,dateChange,isbn]);
    const result1 = await getData(isbn);
    res.render("modify.ejs",{item:result1.rows});
  })

  app.get("/about/:id", async(req,res)=>{

    const isbn=req.params.id;
    const result=await getData(isbn); 
    if(result.rows.length >=1){
         res.render("modify.ejs",{item:result.rows});
    }else{
        await db.query("INSERT INTO details (book_isbn) values ($1)",[isbn]);
        const result= await getData(isbn);
        res.render("modify.ejs",{item:result.rows});
    }

  })
app.get("/back",async (req,res)=>{
    res.redirect("/");
})

app.post("/search",async(req,res)=>{
    var input=req.body.search;
    const result= await db.query("SELECT * FROM books order by id asc; ");
    const search=result.rows.filter((item)=> item.name.toLowerCase().includes(input) ||  item.author.toLowerCase().includes(input))
    res.render("index.ejs",{item:search})
})

app.listen(port,()=>{
    console.log("Server Running at port :"+port);
})
