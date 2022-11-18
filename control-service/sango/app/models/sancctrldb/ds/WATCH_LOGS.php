<?php namespace App\Models\sancctrldb\DS;
use FLY\Model\Algorithm\Model_Controllers;
use FLY_ENV\Util\Model\QueryBuilder;

class WATCH_LOGS extends QueryBuilder {

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

	protected $ACC_ID;

	protected $PERIOD;

	protected $STATUS;


	use Model_Controllers;

	public function __construct($LID="",$ACC_ID="",$PERIOD="",$STATUS="") 
	{
    	parent::__construct($this);
		$this->LID = $LID;
		$this->ACC_ID = $ACC_ID;
		$this->PERIOD = $PERIOD;
		$this->STATUS = $STATUS;

    	$this->pk_names=[ 'LID' ];
    	$this->fk_names=[ 'ACC_ID'=>'ID' ];
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