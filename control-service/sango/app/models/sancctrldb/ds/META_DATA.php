<?php namespace App\Models\sancctrldb\DS;
use FLY\Model\Algorithm\Model_Controllers;
use FLY_ENV\Util\Model\QueryBuilder;

class META_DATA extends QueryBuilder {

/*        
	*******************************************************************************
	* can use transaction here                                                    *
	* example: use TRANSACTION;                                                   *
	* To use a transaction specify the namespace above this model class.          *
	* That is, copy and paste the namespace: use FLY\Model\Algorithm\TRANSACTION; * 
	* right above this model class.                                               *
	*******************************************************************************
*/

	protected $ID;

	protected $URL;

	protected $MTD;

	protected $WITHDRAWAL_STARTS;

	protected $WITHDRAWAL_ENDS;

	protected $JOB_STARTS;

	protected $JOB_ENDS;


	use Model_Controllers;

	public function __construct($ID="",$URL="",$MTD="",$WITHDRAWAL_STARTS="",$WITHDRAWAL_ENDS="",$JOB_STARTS="",$JOB_ENDS="") 
	{
    	parent::__construct($this);
		$this->ID = $ID;
		$this->URL = $URL;
		$this->MTD = $MTD;
		$this->WITHDRAWAL_STARTS = $WITHDRAWAL_STARTS;
		$this->WITHDRAWAL_ENDS = $WITHDRAWAL_ENDS;
		$this->JOB_STARTS = $JOB_STARTS;
		$this->JOB_ENDS = $JOB_ENDS;

    	$this->pk_names=[ 'ID' ];
    	
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