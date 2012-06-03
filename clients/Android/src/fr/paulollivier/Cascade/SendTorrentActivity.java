package fr.paulollivier.Cascade;

import java.net.Socket;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;

public class SendTorrentActivity extends Activity {
	
	Socket s;
	
	
	protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        SharedPreferences sharedpref = getSharedPreferences("Cascade", Activity.MODE_PRIVATE);
        String server = sharedpref.getString("serv_addr", "None");
        Log.d("Preferences", "Server address: " + server);
		Intent intent = getIntent();
		String action = intent.getAction();
		String type = intent.getType();
		
		Uri uri = intent.getParcelableExtra(Intent.EXTRA_STREAM);
		
		Log.d("SendTorrentActivity", "intent to string: "+intent.getStringArrayExtra(name));
		
	}
	
	protected void handleTorrent(Intent intent){
		Uri torrentUri = (Uri) intent.getParcelableExtra(Intent.EXTRA_STREAM);
	}

}
