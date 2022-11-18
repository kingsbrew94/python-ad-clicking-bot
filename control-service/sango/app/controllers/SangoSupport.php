<?php namespace App\Controllers;

use App\Models\sancctrldb\DS\{
INVESTOR_ACCOUNT,
BOT_LOGS  
};
use FLY\Libs\File_API\FileReader;
use FLY\Libs\Request;
use FLY\Libs\Restmodels\Dto;
use FLY\MVC\Controller;
use FLY\Security\KeyGen;

final class SangoSupport extends Controller {

	static function get_accounts_info(Request $req)
	{
		$userId = $req::get('userId');
        $data_index = '[*] ? USER_ID="'.$userId.'" ORDER BY DATE_REGISTERED ASC';
    	return new Dto(true,'',INVESTOR_ACCOUNT::instance()[$data_index]);
	}

	static function get_metadata()
	{
		$meta_data = FileReader::fetchJSON('app/models/meta-data');
		return new Dto($meta_data <> NULL,'',$meta_data);
	}

    static function add_log(Request $req) {
        $logs = new BOT_LOGS();
        $state = true;
        try {
            $lgs = $req::all();
            $lgs['LID'] = KeyGen::primary_key(12,'L%key',true);
            $logs[] = $lgs;
        } catch (Exception $ex) {
            $state = false;
        }
        return new Dto($state, '', $req::all());
    }

    static function logs_exists_today(Request $req) {
        $query = "[*] ? LOGS='";
        $query .= $req::get('LOGS') . "' AND DATE_ADDED LIKE '";
        $query .= $req::get('DATE') . "%'";
        $data = BOT_LOGS::instance()[$query];
        return new Dto($data <> NULL, '', $data);
    }

}