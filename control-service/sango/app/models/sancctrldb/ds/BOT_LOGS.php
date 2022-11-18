<?php namespace App\Models\sancctrldb\DS;
use FLY\Model\Algorithm\Model_Controllers;
use FLY_ENV\Util\Model\QueryBuilder;

class BOT_LOGS extends QueryBuilder {

/*        
	*******************************************************************************
	* can use transaction here                                                    *
	* example: use TRANSACTION;                                                   *
	* To use a transaction specify the namespace above this model class.          *
	* That is, copy and paste the namespace: use FLY\Model\Algorithm\TRANSACTION; * 
	* right above this model class.                                               *
	*******************************************************************************
*/

	protected $LID;

	protected $LOGS;

	protected $DATE_ADDED;


	use Model_Controllers;

	public function __construct($LID="",$LOGS="",$DATE_ADDED="") 
	{
    	parent::__construct($this);
		$this->LID = $LID;
		$this->LOGS = $LOGS;
		$this->DATE_ADDED = $DATE_ADDED;

    	$this->pk_names=[ 'LID' ];
    	
    	$this->apply();
	}


	/**
	 * @return string[]
	 * @Todo It returns the model connection credentials
	 */
	protected function connection(): array
	{
    	return array(
			'host'

				=> 'default',

			'user'

				=> 'default',

			'password'

				=> 'default',

			'model'

				=> 'default'
		);
	}
}