package com.androidsrc.client;

/**
 * Created by bulaa on 10/31/2017.
 */

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.os.AsyncTask;
import android.os.Environment;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.io.FileReader;

import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.UnknownHostException;
import android.os.AsyncTask;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileInputStream;
import android.os.Environment;

public class DisplayDetails extends AsyncTask<Void, Void, Void> {

    String dstAddress;
    int dstPort;
    String response="";
    String response_modified;
    byte[] b;
    //TextView textResponse;
    TextView textResponse;

    DisplayDetails(String addr, int port,TextView textResponse) {
        dstAddress = addr;
        dstPort = port;
        this.textResponse=textResponse;
    }


    @Override
    protected Void doInBackground(Void... arg0) {

        Socket socket = null;

        try {
            socket = new Socket(dstAddress, dstPort);
            Log.d("soc","connected");

            Log.d("soc",socket.getLocalAddress().toString());

            ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(
                    1024);
            byte[] buffer = new byte[1024];

            int bytesRead;
            InputStream inputStream = socket.getInputStream();

			/*
			 * notice: inputStream.read() will block if no data return
			 */
            while ((bytesRead = inputStream.read(buffer)) != -1) {
                byteArrayOutputStream.write(buffer, 0, bytesRead);
                //Log.d("response before",response);
                Log.d("byteArrayOutputStreamb",String.valueOf(byteArrayOutputStream));
                response += byteArrayOutputStream.toString("UTF-8");
                Log.d("response after",response);
                Log.d("byteArrayOutputStreama",String.valueOf(byteArrayOutputStream));
            }

            Log.d("response",response);
            String name=response.split(",")[1];
            String distance=response.split(",")[0];
            String age=response.split(",")[2];
            String relation=response.split(",")[3];
            String profession=response.split(",")[4];

            response_modified= "Name: "+name+"\n"+"Distance: "+distance+"\n"+"Age: "+age+"\n"+"Relation: "+relation+"\n"+"Profession: "+profession;

        } catch (UnknownHostException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            //response = "UnknownHostException: " + e.toString();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            //response = "IOException: " + e.toString();
        } finally {
            if (socket != null) {
                try {
                    socket.close();
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        }
        return null;
    }

    @Override
    protected void onPostExecute(Void result) {

        //super.onPostExecute(result);

            textResponse.setText(response_modified);
            textResponse.setTextColor(Color.BLACK);
            textResponse.setTextAlignment(View.TEXT_ALIGNMENT_CENTER);
            textResponse.setTextSize(15);
            textResponse.setVisibility(View.VISIBLE);



    }

}
