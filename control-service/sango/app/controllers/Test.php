<?php namespace App\Controllers;

use FLY\Libs\Request;
use FLY\MVC\Controller;

final class Test extends Controller {

	static function index(Request $req)
	{
    	// $user = new User;
	///	$user[2] =  ['password' => '8910']; // update table column
		//$user[]   = ['name' => 'Brew', 'password' => 'code2']; // add data to table
		//unset($user['[*]']);  // delete all data
        // var_dump($user['[*]']); // view all data
		// var_dump($user['$[sum(id)]']); // get the sum of ids
		//$user['[ name ] ? id= 1 '] = 'Baah';
		//$user['[name password] ? id=5']   = ['Baah', '1234'];
		// $user['[*] ? id >= 19'] = ['name'=>'Brew'];

		// $user[] = new Client; copy client data and append it user table
    	self::render_view();
    	// code here
	}

}