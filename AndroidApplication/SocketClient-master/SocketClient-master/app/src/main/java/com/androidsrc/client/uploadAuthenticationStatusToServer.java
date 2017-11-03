package com.androidsrc.client;

/**
 * Created by bulaa on 11/1/2017.
 */

import android.graphics.Color;
import android.os.AsyncTask;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Button;
import android.os.Bundle;

import java.io.BufferedOutputStream;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import android.content.res.AssetManager;
import java.io.FileReader;

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
import java.util.ArrayList;
import java.util.List;

import android.os.Environment;

public class uploadAuthenticationStatusToServer extends AsyncTask<Void, Void, Void> {

    String dstAddress;
    int dstPort;
    String response="";
    String response_modified;
    byte[] b;
    //TextView textResponse;
    TextView textResponse;
    String id="";
    EditText authText;
    Button cancel;
    Button ok;

    uploadAuthenticationStatusToServer(String addr, int port,String id,Button can,Button ok,EditText auth) {
        Log.d("con","yes");
        dstAddress = addr;
        dstPort = port;
        //this.textResponse=textResponse;
        this.id=id;
        this.cancel=can;
        this.ok=ok;
        this.authText=auth;
    }


    @Override
    protected Void doInBackground(Void... arg0) {

        Socket socket = null;

        try {
            socket = new Socket(dstAddress, dstPort);
            Log.d("soc upload","connected");

            Log.d("soc upload",socket.getLocalAddress().toString());

            OutputStream outputStream=socket.getOutputStream();

            DataOutputStream dataOutputStream=new DataOutputStream(outputStream);
            Log.d("id",id);
            if(id.equals("cancelButton"))
            {
                Log.d("but check","cancel");
                dataOutputStream.write('0');
            }
            else{
                Log.d("but check","ok");
                dataOutputStream.write('1');
            }

            dataOutputStream.flush();
            Log.d("data",String.valueOf(dataOutputStream));
            dataOutputStream.close();
            outputStream.flush();
            outputStream.close();
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
        cancel.setVisibility(View.INVISIBLE);
        ok.setVisibility(View.INVISIBLE);
        authText.setText("Thank You!");

    }

}

