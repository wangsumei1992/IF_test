import pymysql, configparser, os
from get_data import GetDBDate

host = GetDBDate.host
user = GetDBDate.user
password = GetDBDate.password
db_name = GetDBDate.db_name
port = int(GetDBDate.port)


class DB:
    def __init__(self):
        try:
            self.conn = pymysql.connect(host=host,
                                        port=port,
                                        user=user,
                                        password=password,
                                        db=db_name,
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor
                                        )
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def clear(self, tablename):
        sql = "delete from %s" %tablename
        print(sql)
        with self.conn.cursor() as cursor:
                cursor.execute(sql)
        self.conn.commit()

    def chaxun(self):
        sql = "select * from project where projectid='12567'"
        with self.conn.cursor() as cursor:
                cursor.execute(sql)
                print(cursor.fetchall())

    def insert(self, table_name, test_data):
        data = test_data[table_name]
        for sql in data:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
        self.conn.commit()

    def execute(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()



if __name__ == '__main__':
    datas = {'project':
             ["INSERT INTO `project` (`SignAddr`, `bankAccount`, `bankAccountNumber`, `bankName`, `ProjectID`, `ProjectName`, `FinancingProjectID`, `ProjectStatus`, `apdUserName`, `ProjectCategory`, `CorporeType`, `ProjectType`, `ContractID`, `ContractFullID`, `ContractType`, `LoanContract`, `DisplayWeight`, `MinBidAmount`, `InterestType`, `InterestDaysType`, `RepaymentCalcType`, `PayDateEveryMonth`, `FirstRepaymentDate`, `InterestRate`, `DisplayInterestRate`, `InterestRateDes`, `FinancingMaturityDay`, `FinancingMaturity`, `Amount`, `ServiceFeeRate`, `MunualGuaranteeFeeRate`, `GuaranteeFeeRate`, `LoanManageFeeRate`, `LateFeeRate`, `LateManagerFeeRate`, `GuaranteeCompanyID`, `BorrowerUserID`, `BorrowerPayType`, `IsRealBorrower`, `RealBorrowerUserID`, `RealBorrowerName`, `RealBorrowerIdCard`, `ExpectedOnLineDate`, `AllowInvestAt`, `BidDeadline`, `LastRepaymentDate`, `Area`, `Purpose`, `ProjectDescription`, `ServiceFee`, `FactServiceFee`, `MunualGuaranteeFee`, `GuaranteeFee`, `PaidServiceFee`, `PaidMunualGuaranteeFee`, `PaidGuaranteeFee`, `ReturnMunualGuaranteeFee`, `InvestmentedAmount`, `BidCompletedTime`, `DealDate`, `InterestAmount`, `IsPushToCaihuohuo`, `IsPushToScai`, `IsPushToJinpingmei`, `CreateBy`, `CreateAt`, `UpdateBy`, `UpdateAt`, `OldProjectId`, `LoanId`, `RealUserId`, `PayChannel`, `TransferState`, `TransferTime`, `AutoBidState`, `AutoBidPrecent`, `AutoBidTime`, `PackageId`, `ProjectPackage`, `ProjectNewType`, `CarLoanCompany`, `SourceProjectBeginAt`, `SourceProjectEndAt`, `SourceProjectAmount`, `BorrowerBankAcount`, `IntoPiecesNo`, `houseGuaranteeInfo`, `RepaymentGuarantee`, `RepaymentSource`, `Unicode`, `Address`, `FirstAddress`, `residueFinancingMaturity`, `SeqNo`, `RequestId`, `CutInterest`, `BondManId`, `PartyEId`, `PartyEAddress`, `hasCashLoan`, `cashLoanServiceFee`, `plan_id`, `cust_rating`, `compay_count`, `common_borrower`, `commonborrower_idcard`, `is_overdue`, `is_compay_frozen`) VALUES ('签约地址测试', '', '', '', '60500', '接口测试信2', NULL, 'OPENED', '', 'PersonalCredit', 'general', 'FixedAmount', '', '222', '46926', 'w222', '0', '100.00', 'StartAtBidDeal', NULL, 'EqualInterestPrincipal', NULL, NULL, '0.105000', '10%+0.5%', '', '0', '7.00', '5000.00', '0.00', '0.000000', '0.000000', '0.000000', '0.000000', '0.0000', NULL, '131018', 'BorrowerPay', b'1', '131018', '尔断宰', '410803193906146421', '2018-05-25', '2018-05-25 12:15:00', '2020-05-25 12:15:00', NULL, '1', '资金用途测试', '项目情况测试', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', NULL, NULL, '0.00', b'0', b'0', b'0', '2001', '2018-08-13 10:25:06', '2001', '2018-08-13 10:26:06', NULL, NULL, NULL, NULL, 'NO', NULL, 'ManualBid', '0.00', NULL, NULL, NULL, 'DirectInvestment', '', NULL, NULL, NULL, NULL, '', '还款保障措施测试', '', '还款来源测试', '91110105078544526M', 'BEIJING', '', NULL, '18081310250648699224', '18081310260498825787', NULL, '131991', NULL, '', b'0', NULL, NULL, 'AAA', '0', '', '', '0', '0');",
                #"INSERT INTO `project` (`SignAddr`, `bankAccount`, `bankAccountNumber`, `bankName`, `ProjectID`, `ProjectName`, `FinancingProjectID`, `ProjectStatus`, `apdUserName`, `ProjectCategory`, `CorporeType`, `ProjectType`, `ContractID`, `ContractFullID`, `ContractType`, `LoanContract`, `DisplayWeight`, `MinBidAmount`, `InterestType`, `InterestDaysType`, `RepaymentCalcType`, `PayDateEveryMonth`, `FirstRepaymentDate`, `InterestRate`, `DisplayInterestRate`, `InterestRateDes`, `FinancingMaturityDay`, `FinancingMaturity`, `Amount`, `ServiceFeeRate`, `MunualGuaranteeFeeRate`, `GuaranteeFeeRate`, `LoanManageFeeRate`, `LateFeeRate`, `LateManagerFeeRate`, `GuaranteeCompanyID`, `BorrowerUserID`, `BorrowerPayType`, `IsRealBorrower`, `RealBorrowerUserID`, `RealBorrowerName`, `RealBorrowerIdCard`, `ExpectedOnLineDate`, `AllowInvestAt`, `BidDeadline`, `LastRepaymentDate`, `Area`, `Purpose`, `ProjectDescription`, `ServiceFee`, `FactServiceFee`, `MunualGuaranteeFee`, `GuaranteeFee`, `PaidServiceFee`, `PaidMunualGuaranteeFee`, `PaidGuaranteeFee`, `ReturnMunualGuaranteeFee`, `InvestmentedAmount`, `BidCompletedTime`, `DealDate`, `InterestAmount`, `IsPushToCaihuohuo`, `IsPushToScai`, `IsPushToJinpingmei`, `CreateBy`, `CreateAt`, `UpdateBy`, `UpdateAt`, `OldProjectId`, `LoanId`, `RealUserId`, `PayChannel`, `TransferState`, `TransferTime`, `AutoBidState`, `AutoBidPrecent`, `AutoBidTime`, `PackageId`, `ProjectPackage`, `ProjectNewType`, `CarLoanCompany`, `SourceProjectBeginAt`, `SourceProjectEndAt`, `SourceProjectAmount`, `BorrowerBankAcount`, `IntoPiecesNo`, `houseGuaranteeInfo`, `RepaymentGuarantee`, `RepaymentSource`, `Unicode`, `Address`, `FirstAddress`, `residueFinancingMaturity`, `SeqNo`, `RequestId`, `CutInterest`, `BondManId`, `PartyEId`, `PartyEAddress`, `hasCashLoan`, `cashLoanServiceFee`, `plan_id`, `cust_rating`, `compay_count`, `common_borrower`, `commonborrower_idcard`, `is_overdue`, `is_compay_frozen`) VALUES ('1111', '', '', '', '60496', '接口数据信易融1', NULL, 'OPENED', '', 'PersonalCredit', 'general', 'FixedAmount', '', '1111', '46926', '11111', '0', '100.00', 'StartAtBidDeal', NULL, 'EqualInterestPrincipal', NULL, NULL, '0.115000', '10.5%+1%', '', '0', '6.00', '2000.00', '0.00', '0.000000', '0.000000', '0.000000', '0.000000', '0.0000', NULL, '222925', 'BorrowerPay', b'1', '222925', '榆夫', '410505197001273199', '2018-06-12', '2018-06-12 00:00:25', '2018-06-19 00:00:25', NULL, '1', '1111', '1111', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', NULL, NULL, '0.00', b'0', b'0', b'0', '2001', '2018-06-12 15:24:39', '2001', '2018-06-12 15:31:09', NULL, NULL, NULL, 'Pnr', 'NO', NULL, 'ManualBid', '0.00', NULL, NULL, NULL, 'DirectInvestment', '', '2018-06-12 00:00:00', '2018-08-12 00:00:00', NULL, NULL, '1111', '合作方逾期债权回购', '', '11111', '91110105078544526M', 'BEIJING', '', NULL, '18061215243904210557', '18061215310835944795', NULL, NULL, NULL, '', b'0', NULL, NULL, 'D', '0', '', '', '0', '0');",
             # "INSERT INTO `project` (`SignAddr`, `bankAccount`, `bankAccountNumber`, `bankName`, `ProjectID`, `ProjectName`, `FinancingProjectID`, `ProjectStatus`, `apdUserName`, `ProjectCategory`, `CorporeType`, `ProjectType`, `ContractID`, `ContractFullID`, `ContractType`, `LoanContract`, `DisplayWeight`, `MinBidAmount`, `InterestType`, `InterestDaysType`, `RepaymentCalcType`, `PayDateEveryMonth`, `FirstRepaymentDate`, `InterestRate`, `DisplayInterestRate`, `InterestRateDes`, `FinancingMaturityDay`, `FinancingMaturity`, `Amount`, `ServiceFeeRate`, `MunualGuaranteeFeeRate`, `GuaranteeFeeRate`, `LoanManageFeeRate`, `LateFeeRate`, `LateManagerFeeRate`, `GuaranteeCompanyID`, `BorrowerUserID`, `BorrowerPayType`, `IsRealBorrower`, `RealBorrowerUserID`, `RealBorrowerName`, `RealBorrowerIdCard`, `ExpectedOnLineDate`, `AllowInvestAt`, `BidDeadline`, `LastRepaymentDate`, `Area`, `Purpose`, `ProjectDescription`, `ServiceFee`, `FactServiceFee`, `MunualGuaranteeFee`, `GuaranteeFee`, `PaidServiceFee`, `PaidMunualGuaranteeFee`, `PaidGuaranteeFee`, `ReturnMunualGuaranteeFee`, `InvestmentedAmount`, `BidCompletedTime`, `DealDate`, `InterestAmount`, `IsPushToCaihuohuo`, `IsPushToScai`, `IsPushToJinpingmei`, `CreateBy`, `CreateAt`, `UpdateBy`, `UpdateAt`, `OldProjectId`, `LoanId`, `RealUserId`, `PayChannel`, `TransferState`, `TransferTime`, `AutoBidState`, `AutoBidPrecent`, `AutoBidTime`, `PackageId`, `ProjectPackage`, `ProjectNewType`, `CarLoanCompany`, `SourceProjectBeginAt`, `SourceProjectEndAt`, `SourceProjectAmount`, `BorrowerBankAcount`, `IntoPiecesNo`, `houseGuaranteeInfo`, `RepaymentGuarantee`, `RepaymentSource`, `Unicode`, `Address`, `FirstAddress`, `residueFinancingMaturity`, `SeqNo`, `RequestId`, `CutInterest`, `BondManId`, `PartyEId`, `PartyEAddress`, `hasCashLoan`, `cashLoanServiceFee`, `plan_id`, `cust_rating`, `compay_count`, `common_borrower`, `commonborrower_idcard`, `is_overdue`, `is_compay_frozen`) VALUES ('1111', '', '', '', '61497', '接口数据信易融1', NULL, 'OPENED', '', 'PersonalCredit', 'general', 'FixedAmount', '', '1111', '46926', '11111', '0', '100.00', 'StartAtBidDeal', NULL, 'EqualInterestPrincipal', NULL, NULL, '0.115000', '10.5%+1%', '', '0', '6.00', '2000.00', '0.00', '0.000000', '0.000000', '0.000000', '0.000000', '0.0000', NULL, '222925', 'BorrowerPay', b'1', '222925', '榆夫', '410505197001273199', '2018-06-12', '2018-06-12 00:00:25', '2018-06-19 00:00:25', NULL, '1', '1111', '1111', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '2000.00', NULL, NULL, '0.00', b'0', b'0', b'0', '2001', '2018-06-12 15:24:39', '2001', '2018-06-12 15:31:09', NULL, NULL, NULL, 'Pnr', 'NO', NULL, 'ManualBid', '0.00', NULL, NULL, NULL, 'DirectInvestment', '', '2018-06-12 00:00:00', '2018-08-12 00:00:00', NULL, NULL, '1111', '合作方逾期债权回购', '', '11111', '91110105078544526M', 'BEIJING', '', NULL, '18061215243904210557', '18061215310835944795', NULL, NULL, NULL, '', b'0', NULL, NULL, 'D', '0', '', '', '0', '0');",

              ]
         }
    db = DB()
   # db.clear('project')
    db.insert('project', datas)
    db.close()
