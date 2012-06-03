package fr.paulollivier.Cascade;

import java.net.Socket;
import java.util.Iterator;
import java.util.Set;

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
        Log.d("Preferences", "Getting preferences..");
        SharedPreferences sharedpref = getSharedPreferences("Cascade", Activity.MODE_PRIVATE);
        String server = sharedpref.getString("serv_addr", "None");
        Log.d("Preferences", "Server address: " + server);
		Intent intent = getIntent();
		while(savedInstanceState.keySet().iterator().hasNext())
			Log.d("Bundle", savedInstanceState.keySet().iterator().next());
		
		Log.d("Intent", "Getting all keys");
		Iterator<String> keysit = intent.getExtras().keySet().iterator();
		while(keysit.hasNext()){
			Log.d("Intent Keys", keysit.next());
		}
		Log.d("Intent", "Done");
		
		Log.d("Torrent", "Getting Uri from intent...");
		try {
			Uri uri = (Uri)intent.getParcelableExtra(Intent.EXTRA_STREAM);
			Log.d("SENDTORACT", "torrent uri: " + uri.toString());
		}
		catch(Exception e){
			Log.e("Torrent", e.getLocalizedMessage());
		}
		
	}
	
	protected void handleTorrent(Intent intent){
		Uri torrentUri = (Uri) intent.getParcelableExtra(Intent.EXTRA_STREAM);
	}

}
