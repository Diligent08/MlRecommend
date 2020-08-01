package com.example.dell;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.method.ScrollingMovementMethod;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class MainActivity extends AppCompatActivity {
    TextView e1;
    TextView e2;
    Button b1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        e1=findViewById(R.id.textView2);
        e2=findViewById(R.id.textView3);
        b1=findViewById(R.id.button3);
    }
    public void load1(View v)
    {
        e1.setMovementMethod(new ScrollingMovementMethod());
        String data=" ";
        StringBuffer  sbuffer=new StringBuffer();
        InputStream is=this.getResources().openRawResource(R.raw.text4);
        BufferedReader reader=new BufferedReader(new InputStreamReader(is));

        if(is!=null){
            try {


                while ((data = reader.readLine()) != null) {
                    sbuffer.append(data +"      ");
                }
                e1.setText(sbuffer);
                is.close();
            } catch (IOException e) {
                e.printStackTrace();
            }


        }




    }
    public void recc(View v)
    {
        e2.setMovementMethod(new ScrollingMovementMethod());
        String data=" ";
        StringBuffer  sbuffer=new StringBuffer();
        InputStream is=this.getResources().openRawResource(R.raw.textfile);
        BufferedReader reader=new BufferedReader(new InputStreamReader(is));

        if(is!=null){
            try {


                while ((data = reader.readLine()) != null) {
                    sbuffer.append(data + "     ");
                }
                e2.setText(sbuffer);
                is.close();
            } catch (IOException e) {
                e.printStackTrace();
            }


        }




    }
    public void func1(View v)
    {
        Toast.makeText(this,"Your comments have been recorded",Toast.LENGTH_LONG).show();


    }
}
