
#  ECPay 物流 SDK 
# 
#  @author		David Chen <david2003542@gmail.com>
#  @version		GIT: <david2003542/ECPayLogistic_PYTHON>


#  物流類型
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class LogisticsType:
    CVS = 'CVS' #超商取貨
    HOME = 'Home' #宅配



#  物流子類型
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class LogisticsSubType:
    TCAT = 'TCAT' #黑貓(宅配)
    ECAN = 'ECAN' #宅配通
    FAMILY = 'FAMI' #全家
    UNIMART = 'UNIMART' #統一超商
    HILIFE = 'HILIFE' #萊爾富
    FAMILY_C2C = 'FAMIC2C' #全家店到店
    UNIMART_C2C = 'UNIMARTC2C' #統一超商寄貨便
    HILIFE_C2C = 'HILIFEC2C' #萊爾富富店到店



#  是否代收貨款
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class IsCollection:
    YES = 'Y' #貨到付款
    NO = 'N' #僅配送



#  使用設備
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class Device:
    PC = 0 #PC
    MOBILE = 1 #行動裝置



#  測試廠商編號
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class ECPayTestMerchantID:
    B2C = '2000132' #B2C
    C2C = '2000933' #C2C



#  正式環境網址
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class ECPayURL:
    CVS_MAP = 'https://logistics.ecpay.com.tw/Express/map' #電子地圖
    SHIPPING_ORDER = 'https://logistics.ecpay.com.tw/Express/Create' #物流訂單建立
    HOME_RETURN_ORDER = 'https://logistics.ecpay.com.tw/Express/ReturnHome' #宅配逆物流訂單
    UNIMART_RETURN_ORDER = 'https://logistics.ecpay.com.tw/express/ReturnUniMartCVS' #超商取貨逆物流訂單(統一超商B2C)
    HILIFE_RETURN_ORDER = 'https://logistics.ecpay.com.tw/express/ReturnHiLifeCVS' #超商取貨逆物流訂單(萊爾富超商B2C)
    FAMILY_RETURN_ORDER = 'https://logistics.ecpay.com.tw/express/ReturnCVS' #超商取貨逆物流訂單(全家超商B2C)
    FAMILY_RETURN_CHECK = 'https://logistics.ecpay.com.tw/Helper/LogisticsCheckAccoounts' #全家逆物流核帳(全家超商B2C)
    UNIMART_UPDATE_LOGISTICS_INFO = 'https://logistics.ecpay.com.tw/Helper/UpdateShipmentInfo' #統一修改物流資訊(全家超商B2C)
    UNIMART_UPDATE_STORE_INFO = 'https://logistics.ecpay.com.tw/Express/UpdateStoreInfo' #更新門市(統一超商C2C)
    UNIMART_CANCEL_LOGISTICS_ORDER = 'https://logistics.ecpay.com.tw/Express/CancelC2COrder' #取消訂單(統一超商C2C)
    QUERY_LOGISTICS_INFO = 'https://logistics.ecpay.com.tw/Helper/QueryLogisticsTradeInfo/V2' #物流訂單查詢
    PRINT_TRADE_DOC = 'https://logistics.ecpay.com.tw/helper/printTradeDocument' #產生托運單(宅配)/一段標(超商取貨)
    PRINT_UNIMART_C2C_BILL = 'https://logistics.ecpay.com.tw/Express/PrintUniMartC2COrderInfo' #列印繳款單(統一超商C2C)
    PRINT_FAMILY_C2C_BILL = 'https://logistics.ecpay.com.tw/Express/PrintFAMIC2COrderInfo' #全家列印小白單(全家超商C2C)
    PRINT_HILIFE_C2C_BILL = 'https://logistics.ecpay.com.tw/Express/PrintHILIFEC2COrderInfo' #萊爾富列印小白單(萊爾富超商C2C)
    CREATE_TEST_DATA = 'https://logistics.ecpay.com.tw/Express/CreateTestData' #產生 B2C 測標資料



#  測試環境網址
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class ECPayTestURL:
    CVS_MAP = 'https://logistics-stage.ecpay.com.tw/Express/map' #電子地圖
    SHIPPING_ORDER = 'https://logistics-stage.ecpay.com.tw/Express/Create' #物流訂單建立
    HOME_RETURN_ORDER = 'https://logistics-stage.ecpay.com.tw/Express/ReturnHome' #宅配逆物流訂單
    UNIMART_RETURN_ORDER = 'https://logistics-stage.ecpay.com.tw/express/ReturnUniMartCVS' #超商取貨逆物流訂單(統一超商B2C)
    HILIFE_RETURN_ORDER = 'https://logistics-stage.ecpay.com.tw/express/ReturnHiLifeCVS' #超商取貨逆物流訂單(萊爾富超商B2C)
    FAMILY_RETURN_ORDER = 'https://logistics-stage.ecpay.com.tw/express/ReturnCVS' #超商取貨逆物流訂單(全家超商B2C)
    FAMILY_RETURN_CHECK = 'https://logistics-stage.ecpay.com.tw/Helper/LogisticsCheckAccoounts' #全家逆物流核帳(全家超商B2C)
    UNIMART_UPDATE_LOGISTICS_INFO = 'https://logistics-stage.ecpay.com.tw/Helper/UpdateShipmentInfo' #統一修改物流資訊(全家超商B2C)
    UNIMART_UPDATE_STORE_INFO = 'https://logistics-stage.ecpay.com.tw/Express/UpdateStoreInfo' #更新門市(統一超商C2C)
    UNIMART_CANCEL_LOGISTICS_ORDER = 'https://logistics-stage.ecpay.com.tw/Express/CancelC2COrder' #取消訂單(統一超商C2C)
    QUERY_LOGISTICS_INFO = 'https://logistics-stage.ecpay.com.tw/Helper/QueryLogisticsTradeInfo/V2' #物流訂單查詢
    PRINT_TRADE_DOC = 'https://logistics-stage.ecpay.com.tw/helper/printTradeDocument' #產生托運單(宅配)/一段標(超商取貨)
    PRINT_UNIMART_C2C_BILL = 'https://logistics-stage.ecpay.com.tw/Express/PrintUniMartC2COrderInfo' #列印繳款單(統一超商C2C)
    PRINT_FAMILY_C2C_BILL = 'https://logistics-stage.ecpay.com.tw/Express/PrintFAMIC2COrderInfo' #全家列印小白單(全家超商C2C)
    PRINT_HILIFE_C2C_BILL = 'https://logistics-stage.ecpay.com.tw/Express/PrintHILIFEC2COrderInfo' #萊爾富列印小白單(萊爾富超商C2C)
    CREATE_TEST_DATA = 'https://logistics-stage.ecpay.com.tw/Express/CreateTestData' #產生 B2C 測標資料



#  溫層
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class Temperature:
    ROOM = '0001' #常溫
    REFRIGERATION = '0002' #冷藏
    FREEZE = '0003' #冷凍



#  距離
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class Distance:
    SAME = '00' #同縣市
    OTHER = '01' #外縣市
    ISLAND = '02' #離島



#  規格
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class Specification:
    CM_60 = '0001' #60cm
    CM_90 = '0002' #90cm
    CM_120 = '0003' #120cm
    CM_150 = '0004' #150cm



#  預計取件時段
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class ScheduledPickupTime:
    TIME_9_12 = '1' #9~12時
    TIME_12_17 = '2' #12~17時
    TIME_17_20 = '3' #17~20時
    UNLIMITED = '4' #不限時


#  預定送達時段
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class ScheduledDeliveryTime:
    TIME_9_12 = '1' #9~12時
    TIME_12_17 = '2' #12~17時
    TIME_17_20 = '3' #17~20時
    UNLIMITED = '4' #不限時
    TIME_20_21 = '5' #20~21時(需限定區域)
    TIME_9_17 = '12' #早午 9~17
    TIME_9_12_17_20 = '13' #早晚 9~12 & 17~20
    TIME_13_20 = '23' #午晚 13~20



#  門市類型
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class StoreType:
    RECIVE_STORE = '01' #取件門市
    RETURN_STORE = '02' #退件門市


##HERE OKAY


#  物流 SDK
#
# @author		David Chen <david2003542@gmail.com>
# @category	Options
# @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
class ECPayLogistics:
    ServiceURL = '' 
    HashKey = '' 
    HashIV = '' 
    Send = {} 
    SendExtend = '' 
    PostParams = {} 
    Encode = 'UTF-8' 
    
    
    
    #  電子地圖
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @param		String ButtonDesc 按鈕顯示名稱
    # @param		String Target 表單 action 目標
    # @return		String
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def CvsMap(ButtonDesc = '電子地圖', Target = '_self'):
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'MerchantTradeNo':'',
            'LogisticsSubType':'',
            'IsCollection':'',
            'ServerReplyURL':'',
            'ExtraData':'',
            'Device':Device.PC
        }
        PostParams = GetPostParams(Send, ParamList) 
        PostParams['LogisticsType'] = LogisticsType.CVS 
        
        #參數檢查
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('CVS_MAP') 
        ValidateLogisticsSubType() 
        ValidateIsCollection() 
        ValidateURL('ServerReplyURL', PostParams['ServerReplyURL']) 
        ValidateString('ExtraData', PostParams['ExtraData'], 20, true) 
        ValidateDevice(true) 
        
        return GenPostHTML(ButtonDesc, Target) 
    
    
    #  物流訂單建立
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @param		String ButtonDesc 按鈕顯示名稱
    # @param		String Target 表單 action 目標
    # @return		String
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def CreateShippingOrder(ButtonDesc = '物流訂單建立', Target = '_self'):
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'MerchantTradeNo':'',
            'MerchantTradeDate':'',
            'LogisticsType':'',
            'LogisticsSubType':'',
            'GoodsAmount':0,
            'CollectionAmount':0,
            'IsCollection':IsCollection.NO,
            'GoodsName':'',
            'SenderName':'',
            'SenderPhone':'',
            'SenderCellPhone':'',
            'ReceiverName':'',
            'ReceiverPhone':'',
            'ReceiverCellPhone':'',
            'ReceiverEmail':'',
            'TradeDesc':'',
            'ServerReplyURL':'',
            'ClientReplyURL':'',
            'LogisticsC2CReplyURL':'',
            'Remark':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        MinAmount = 1  #金額下限
        MaxAmount = 20000  #金額上限
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('SHIPPING_ORDER') 
        ValidateMerchantTradeDate() 
        ValidateLogisticsType() 
        ValidateLogisticsSubType() 
        
        #依不同的物流類型(LogisticsType)設定專屬參數並檢查
        if PostParams['LogisticsType'] == LogisticsType.CVS:
            CvsParamList = {
                'ReceiverStoreID':'',
                'ReturnStoreID':''
            }
            PostParams = GetPostParams(SendExtend, CvsParamList, PostParams) 
        
            ValidateMixTypeID('ReceiverStoreID', PostParams['ReceiverStoreID'], 6) 
            ValidateMixTypeID('ReturnStoreID', PostParams['ReturnStoreID'], 6, true) 
        if PostParams['LogisticsType'] == LogisticsType.HOME:
            HomeParamList = {
                'SenderZipCode':'',
                'SenderAddress':'',
                'ReceiverZipCode':'',
                'ReceiverAddress':'',
                'Temperature':Temperature.ROOM,
                'Distance':Distance.SAME,
                'Specification':Specification.CM_60,
                'ScheduledDeliveryTime':'',
                'ScheduledDeliveryDate':'',
                'PackageCount':0
            } 
            PostParams = GetPostParams(SendExtend, HomeParamList, PostParams) 
            PostParams['ScheduledPickupTime'] = ScheduledPickupTime.UNLIMITED 
            
            ValidateZipCode('SenderZipCode', PostParams['SenderZipCode']) 
            ValidateAddress('SenderAddress', PostParams['SenderAddress'], 6, 60) 
            ValidateZipCode('ReceiverZipCode', PostParams['ReceiverZipCode']) 
            ValidateAddress('ReceiverAddress', PostParams['ReceiverAddress'], 6, 60) 
            ValidateTemperature() 
            ValidateDistance() 
            ValidateSpecification() 
            ValidateScheduledDeliveryTime(true) 
        
        ValidateAmount('GoodsAmount', PostParams['GoodsAmount']) 
        if PostParams['LogisticsSubType'] == LogisticsSubType.UNIMART or PostParams['LogisticsSubType'] == LogisticsSubType.UNIMART_C2C:
            #物流子類型(LogisticsSubType)為統一超商(UNIMART)或統一超商交貨便(UNIMARTC2C)時，商品金額範圍為1~19,999元
            MaxAmount = 19999 
        if PostParams['GoodsAmount'] < MinAmount or PostParams['GoodsAmount'] > MaxAmount:
            raise Exception('Invalid GoodsAmount.') 
        
        ValidateIsCollection(true) 
        if PostParams['IsCollection'] == IsCollection.NO:
            #若設定為僅配送，清除代收金額
            unset(PostParams['CollectionAmount']) 
        else:
            ValidateAmount('CollectionAmount', PostParams['CollectionAmount']) 
            if PostParams['CollectionAmount'] < MinAmount or PostParams['CollectionAmount'] > MaxAmount:
                raise Exception('Invalid CollectionAmount.') 
            
        
        if PostParams['LogisticsSubType'] == LogisticsSubType.HILIFE_C2C or PostParams['LogisticsSubType'] == LogisticsSubType.UNIMART_C2C:
            #物流子類型(LogisticsSubType)為萊爾富店到店(HILIFEC2C)、 統一超商交貨便(UNIMARTC2C)時，不可為空
            ValidateString('GoodsName', PostParams['GoodsName'], 60) 
        else:
            ValidateString('GoodsName', PostParams['GoodsName'], 60, true) 
        
        ValidateString('SenderName', PostParams['SenderName'], 10) 
        ValidatePhoneNumber('SenderPhone', PostParams['SenderPhone'], true) 
        ValidateCellphoneNumber('SenderCellPhone', PostParams['SenderCellPhone'], true) 
        if PostParams['LogisticsType'] == LogisticsType.HOME:
            #物流類型(LogisticsType)為宅配(Home)時，寄件人電話(SenderPhone)或寄件人手機(SenderCellPhone)不可為空
            if PostParams['SenderPhone'] and PostParams['SenderCellPhone']:
                raise Exception('SenderPhone or SenderCellPhone is required when LogisticsType is Home.')
        elif PostParams['LogisticsSubType'] == LogisticsSubType.HILIFE_C2C or PostParams['LogisticsSubType'] == LogisticsSubType.UNIMART_C2C:
            #物流子類型(LogisticsSubType)為統一超商交貨便(UNIMARTC2C)、萊爾富店到店(HILIFEC2C)時，寄件人手機(SenderCellPhone)不可為空
            if PostParams['SenderCellPhone']:
                raise Exception('SenderCellPhone is required when LogisticsSubType is UNIMARTC2C or HILIFEC2C.')
        
        ValidateString('ReceiverName', PostParams['ReceiverName'], 10) 
        ValidatePhoneNumber('ReceiverPhone', PostParams['ReceiverPhone'], true) 
        ValidateCellphoneNumber('ReceiverCellPhone', PostParams['ReceiverCellPhone'], true) 
        if PostParams['LogisticsType'] == LogisticsType.HOME:
            #物流類型(LogisticsType)為宅配(Home)時，收件人電話(ReceiverPhone)或收件人手機(ReceiverCellPhone)不可為空
            if PostParams['ReceiverPhone'] and PostParams['ReceiverCellPhone']:
                raise Exception('ReceiverPhone or ReceiverCellPhone is required when LogisticsType is Home.') 
        else:
            #物流子類型(LogisticsSubType)為統一超商(UNIMART)、全家(FAMILY)、萊爾富(HILIFE)、統一超商交貨便(UNIMARTC2C)、全家超商店到店(FAMILYC2C)、萊爾富富店到店(HILIFEC2C)時，收件人手機(ReceiverCellPhone)不可為空
            if PostParams['ReceiverCellPhone']:
                raise Exception('ReceiverCellPhone is required.')

        if PostParams['LogisticsSubType'] == LogisticsSubType.ECAN and PostParams['Temperature'] != Temperature.ROOM:
            #物流子類型為宅配通(ECAN)時，溫層(Temperature)只能用常溫(ROOM)
            raise Exception('Temperature should be ROOM when LogisticsSubType is ECAN.') 

        if PostParams['LogisticsSubType'] == LogisticsSubType.ECAN and date('Ymd', strtotime(PostParams['ScheduledDeliveryDate'])) < date('Ymd', strtotime('+3 day')):
            #指定送達日期為該訂單建立時間 + 3 天
            raise Exception('ScheduledDeliveryDate should be the time that create order + 3 day.') 
        
        ValidateEmail('ReceiverEmail', PostParams['ReceiverEmail'], 50, true) 
        ValidateString('TradeDesc', PostParams['TradeDesc'], 200, true) 
        ValidateURL('ServerReplyURL', PostParams['ServerReplyURL']) 
        ValidateURL('ClientReplyURL', PostParams['ClientReplyURL'], 200, true) 
        
        if PostParams['LogisticsSubType'] == LogisticsSubType.UNIMART_C2C:
            #物流子類型(LogisticsSubType)為統一超商交貨便(UNIMARTC2C)時，此欄位不可為空
            ValidateURL('LogisticsC2CReplyURL', PostParams['LogisticsC2CReplyURL']) 
        else:
            ValidateURL('LogisticsC2CReplyURL', PostParams['LogisticsC2CReplyURL'], 200, true) 
        
        ValidateString('Remark', PostParams['Remark'], 200, true) 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #物流類型(LogisticsType)為宅配(Home)且溫層(Temperature)為冷凍(0003)時，規格(Specification)不可為 150cm(0004)
        if PostParams['LogisticsType'] == LogisticsType.HOME and PostParams['Temperature'] == Temperature.FREEZE:
            if PostParams['Specification'] == Specification.CM_150:
                raise Exception('Specification could not be 150cm(0004) when LogisticsType is Home and Temperature is FREEZE(0003).')
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        return GenPostHTML(ButtonDesc, Target)
    
    
    #  幕後物流訂單建立
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def BGCreateShippingOrder():
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'MerchantTradeNo':'',
            'MerchantTradeDate':'',
            'LogisticsType':'',
            'LogisticsSubType':'',
            'GoodsAmount':0,
            'CollectionAmount':0,
            'IsCollection':IsCollection.NO,
            'GoodsName':'',
            'SenderName':'',
            'SenderPhone':'',
            'SenderCellPhone':'',
            'ReceiverName':'',
            'ReceiverPhone':'',
            'ReceiverCellPhone':'',
            'ReceiverEmail':'',
            'TradeDesc':'',
            'ServerReplyURL':'',
            'LogisticsC2CReplyURL':'',
            'Remark':'',
            'PlatformID':''
        } 
        
        #幕後物流訂單建立不可設定Client端回覆網址(ClientReplyURL)
        if not Send['ClientReplyURL']:
            raise Exception('ClientReplyURL should be null.') 
        
        
        PostParams = GetPostParams(Send, ParamList) 
        MinAmount = 1  #金額下限
        MaxAmount = 20000  #金額上限
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('SHIPPING_ORDER') 
        ValidateMerchantTradeDate() 
        ValidateLogisticsType() 
        ValidateLogisticsSubType() 
        
        #依不同的物流類型(LogisticsType)設定專屬參數並檢查
        if PostParams['LogisticsType'] == LogisticsType.CVS:
            CvsParamList = {
                'ReceiverStoreID':'',
                'ReturnStoreID':''
            } 
            PostParams = GetPostParams(SendExtend, CvsParamList, PostParams) 
        
            ValidateMixTypeID('ReceiverStoreID', PostParams['ReceiverStoreID'], 6) 
            ValidateMixTypeID('ReturnStoreID', PostParams['ReturnStoreID'], 6, true) 
        if PostParams['LogisticsType'] == LogisticsType.HOME: 
            HomeParamList = {
                'SenderZipCode':'',
                'SenderAddress':'',
                'ReceiverZipCode':'',
                'ReceiverAddress':'',
                'Temperature':Temperature.ROOM,
                'Distance':Distance.SAME,
                'Specification':Specification.CM_60,
                'ScheduledDeliveryTime':'',
                'ScheduledDeliveryDate':'',
                'PackageCount':0
            }
            PostParams = GetPostParams(SendExtend, HomeParamList, PostParams) 
            PostParams['ScheduledPickupTime'] = ScheduledPickupTime.UNLIMITED 
            
            ValidateZipCode('SenderZipCode', PostParams['SenderZipCode']) 
            ValidateAddress('SenderAddress', PostParams['SenderAddress'], 6, 60) 
            ValidateZipCode('ReceiverZipCode', PostParams['ReceiverZipCode']) 
            ValidateAddress('ReceiverAddress', PostParams['ReceiverAddress'], 6, 60) 
            ValidateTemperature() 
            ValidateDistance() 
            ValidateSpecification() 
            ValidateScheduledDeliveryTime(true)
        
        ValidateAmount('GoodsAmount', PostParams['GoodsAmount']) 
        if PostParams['LogisticsSubType'] == LogisticsSubType.UNIMART or PostParams['LogisticsSubType'] == LogisticsSubType.UNIMART_C2C:
            #物流子類型(LogisticsSubType)為統一超商(UNIMART)或統一超商交貨便(UNIMARTC2C)時，商品金額範圍為1~19,999元
            MaxAmount = 19999 
        
        if PostParams['GoodsAmount'] < MinAmount or PostParams['GoodsAmount'] > MaxAmount:
            raise Exception('Invalid GoodsAmount.') 
        
        ValidateIsCollection(true) 
        if PostParams['IsCollection'] == IsCollection.NO:
            #若設定為僅配送，清除代收金額
            unset(PostParams['CollectionAmount']) 
        else:
            ValidateAmount('CollectionAmount', PostParams['CollectionAmount']) 
            if PostParams['CollectionAmount'] < MinAmount or PostParams['CollectionAmount'] > MaxAmount:
                raise Exception('Invalid CollectionAmount.') 
        
        if PostParams['LogisticsSubType'] == LogisticsSubType.HILIFE_C2C or PostParams['LogisticsSubType'] == LogisticsSubType.UNIMART_C2C:
            #物流子類型(LogisticsSubType)為萊爾富店到店(HILIFEC2C)、 統一超商交貨便(UNIMARTC2C)時，不可為空
            ValidateString('GoodsName', PostParams['GoodsName'], 60) 
        else:
            ValidateString('GoodsName', PostParams['GoodsName'], 60, true) 
        
        
        ValidateString('SenderName', PostParams['SenderName'], 10) 
        ValidatePhoneNumber('SenderPhone', PostParams['SenderPhone'], true) 
        ValidateCellphoneNumber('SenderCellPhone', PostParams['SenderCellPhone'], true) 
        if PostParams['LogisticsType'] == LogisticsType.HOME:
            #物流類型(LogisticsType)為宅配(Home)時，寄件人電話(SenderPhone)或寄件人手機(SenderCellPhone)不可為空
            if PostParams['SenderPhone'] and PostParams['SenderCellPhone']:
                raise Exception('SenderPhone or SenderCellPhone is required when LogisticsType is Home.') 
            
        elif PostParams['LogisticsSubType'] == LogisticsSubType.HILIFE_C2C or PostParams['LogisticsSubType'] == LogisticsSubType.UNIMART_C2C:
            #物流子類型(LogisticsSubType)為統一超商交貨便(UNIMARTC2C)、萊爾富店到店(HILIFEC2C)時，寄件人手機(SenderCellPhone)不可為空
            if PostParams['SenderCellPhone']:
                raise Exception('SenderCellPhone is required when LogisticsSubType is UNIMARTC2C or HILIFEC2C.') 
            
        
        
        ValidateString('ReceiverName', PostParams['ReceiverName'], 10) 
        ValidatePhoneNumber('ReceiverPhone', PostParams['ReceiverPhone'], true) 
        ValidateCellphoneNumber('ReceiverCellPhone', PostParams['ReceiverCellPhone'], true) 
        if PostParams['LogisticsType'] == LogisticsType.HOME:
            #物流類型(LogisticsType)為宅配(Home)時，收件人電話(ReceiverPhone)或收件人手機(ReceiverCellPhone)不可為空
            if PostParams['ReceiverPhone'] and PostParams['ReceiverCellPhone']:
                raise Exception('ReceiverPhone or ReceiverCellPhone is required when LogisticsType is Home.') 
        else:
            #物流子類型(LogisticsSubType)為統一超商(UNIMART)、全家(FAMILY)、萊爾富(HILIFE)、統一超商交貨便(UNIMARTC2C)、全家超商店到店(FAMILYC2C)、萊爾富富店到店(HILIFEC2C)時，收件人手機(ReceiverCellPhone)不可為空
            if PostParams['ReceiverCellPhone']:
                raise Exception('ReceiverCellPhone is required.') 
            
        
        
        if PostParams['LogisticsSubType'] == LogisticsSubType.ECAN and PostParams['Temperature'] != Temperature.ROOM:
            #物流子類型為宅配通(ECAN)時，溫層(Temperature)只能用常溫(ROOM)
            raise Exception('Temperature should be ROOM when LogisticsSubType is ECAN.') 
        
        if PostParams['LogisticsSubType'] == LogisticsSubType.ECAN and date('Ymd', strtotime(PostParams['ScheduledDeliveryDate'])) < date('Ymd', strtotime('+3 day')):
            #指定送達日期為該訂單建立時間 + 3 天
            raise Exception('ScheduledDeliveryDate should be the time that create order + 3 day.') 
        

        ValidateEmail('ReceiverEmail', PostParams['ReceiverEmail'], 50, true) 
        ValidateString('TradeDesc', PostParams['TradeDesc'], 200, true) 
        ValidateURL('ServerReplyURL', PostParams['ServerReplyURL']) 
        
        if PostParams['LogisticsSubType'] == LogisticsSubType.UNIMART_C2C:
            #物流子類型(LogisticsSubType)為統一超商交貨便(UNIMARTC2C)時，此欄位不可為空
            ValidateURL('LogisticsC2CReplyURL', PostParams['LogisticsC2CReplyURL']) 
        else:
            ValidateURL('LogisticsC2CReplyURL', PostParams['LogisticsC2CReplyURL'], 200, true) 
        
        
        ValidateString('Remark', PostParams['Remark'], 200, true) 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #物流類型(LogisticsType)為宅配(Home)且溫層(Temperature)為冷凍(0003)時，規格(Specification)不可為 150cm(0004)
        if PostParams['LogisticsType'] == LogisticsType.HOME and PostParams['Temperature'] == Temperature.FREEZE:
            if PostParams['Specification'] == Specification.CM_150:
                raise Exception('Specification could not be 0004 when LogisticsType is Home and Temperature is 0003.') 
            
        
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 

        #urlencode
        for key, value in PostParams.items():
            PostParams[key] = urlencode(value) 
        
        
        #解析回傳結果
        #正確：1|MerchantID=XXX&MerchantTradeNo=XXX&RtnCode=XXX&RtnMsg=XXX&AllPayLogisticsID=XXX&LogisticsType=XXX&LogisticsSubType=XXX&GoodsAmount=XXX&UpdateStatusDate=XXX&ReceiverName=XXX&ReceiverPhone=XXX&ReceiverCellPhone=XXX&ReceiverEmail=XXX&ReceiverAddress=XXX&CVSPaymentNo=XXX&CVSValidationNo=XXX &CheckMacValue=XXX
        #錯誤：0|ErrorMessage
        Feedback = ECPay_IO.ServerPost(PostParams, ServiceURL) 
        Pieces = explode('|', Feedback) 
        Result = {} 
        Result['ResCode'] = Pieces[0] 
        if Result['ResCode']:
            RtnCont = {} 
            parse_str(Pieces[1], RtnCont) 
            Result = Result + RtnCont
        else:
            Result['ErrorMessage'] = Pieces[1] 
        
        
        return Result 
    

    
    #  回傳 CheckMacValue 檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @param		Array Feedback ECPay 回傳資料
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def CheckOutFeedback(Feedback = {}):
        
        ValidateHashKey() 
        ValidateHashIV() 
        
        if Feedback:
            raise Exception('Feedback is required.') 
        
        
        if not isset(Feedback['CheckMacValue']):
            raise Exception('Feedback CheckMacValue is required.') 
        else:
            FeedbackCheckMacValue = Feedback['CheckMacValue'] 
            unset(Feedback['CheckMacValue']) 
            unset(Feedback['ResCode']) 
            unset(Feedback['ErrorMessage']) 
            CheckMacValue = ECPay_CheckMacValue.generate(Feedback, HashKey, HashIV) 
            if CheckMacValue != FeedbackCheckMacValue:
                raise Exception('CheckMacValue verify fail.') 
            
        
    

    
    #  宅配逆物流訂單產生
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def CreateHomeReturnOrder():
        
        #參數初始化
        ParamList = {
            'MerchantID':'',			
            'AllPayLogisticsID':'',
            'LogisticsSubType':'',
            'ServerReplyURL':'',
            'SenderName':'',
            'SenderPhone':'',
            'SenderCellPhone':'',
            'SenderZipCode':'',
            'SenderAddress':'',
            'ReceiverName':'',
            'ReceiverPhone':'',
            'ReceiverCellPhone':'',
            'ReceiverZipCode':'',
            'ReceiverAddress':'',
            'GoodsAmount':'',
            'GoodsName':'',
            'Temperature':Temperature.ROOM,
            'Distance':Distance.SAME,
            'Specification':Specification.CM_60,
            'ScheduledPickupTime':ScheduledPickupTime.UNLIMITED,
            'ScheduledDeliveryTime':'',
            'ScheduledDeliveryDate':'',
            'PackageCount':0,
            'Remark':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        PostParams['ScheduledPickupTime'] = ScheduledPickupTime.UNLIMITED  #預定取件時段(ScheduledPickupTime)固定為不限時
        IsAllpayLogisticsIdEmpty = False  #物流交易編號(AllPayLogisticsID)是否為空
        IsAllowEmpty = true 
        MinAmount = 1  #金額下限
        MaxAmount = 20000  #金額上限
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('HOME_RETURN_ORDER') 
        
        ValidateID('AllPayLogisticsID', PostParams['AllPayLogisticsID'], 20, true) 

        ValidateLogisticsSubType(true) 

        #物流交易編號(AllPayLogisticsID)與物流子類型(LogisticsSubType)擇一不可為空
        if PostParams['AllPayLogisticsID']:
            IsAllpayLogisticsIdEmpty = true 
        
        if IsAllpayLogisticsIdEmpty == true and PostParams['LogisticsSubType']:
            raise Exception('One of AllPayLogisticsID and LogisticsSubType is required.') 
        
        
        ValidateURL('ServerReplyURL', PostParams['ServerReplyURL']) 
        
        #物流交易編號(AllPayLogisticsID)為空值時，退貨人姓名(SenderName)不可為空。
        if IsAllpayLogisticsIdEmpty:
            IsAllowEmpty = False 
        
        ValidateString('SenderName', PostParams['SenderName'], 10, IsAllowEmpty) 
        
        ValidatePhoneNumber('SenderPhone', PostParams['SenderPhone'], true) 
        ValidateCellphoneNumber('SenderCellPhone', PostParams['SenderCellPhone'], true) 
        #物流交易編號(AllPayLogisticsID)為空值時，退貨人電話(SenderPhone)與退貨人手機(SenderCellPhone)擇一不可為空。
        if IsAllpayLogisticsIdEmpty:
            if PostParams['SenderPhone'] and PostParams['SenderCellPhone']:
                raise Exception('One of SenderPhone and SenderCellPhone is required.') 
            
        
        
        #物流交易編號(AllPayLogisticsID)為空值時，退貨人郵遞區號(SenderZipCode)不可為空。
        ValidateZipCode('SenderZipCode', PostParams['SenderZipCode'], IsAllowEmpty) 
        
        #物流交易編號(AllPayLogisticsID)為空值時，SenderAddress(SenderAddress)不可為空。
        ValidateAddress('SenderAddress', PostParams['SenderAddress'], 6, 60, IsAllowEmpty) 
        
        #若物流交易編號(AllPayLogisticsID)為空值時，收件人姓名(ReceiverName)不可為空。
        ValidateString('ReceiverName', PostParams['ReceiverName'], 10, IsAllowEmpty) 
        
        ValidatePhoneNumber('ReceiverPhone', PostParams['ReceiverPhone'], 20, true) 
        ValidateCellphoneNumber('ReceiverCellPhone', PostParams['ReceiverCellPhone'], 20, true) 
        #物流交易編號(AllPayLogisticsID)為空值時，收件人電話(ReceiverPhone)與收件人手機(ReceiverCellPhone)擇一不可為空。
        if IsAllpayLogisticsIdEmpty:
            if PostParams['ReceiverPhone'] and PostParams['ReceiverCellPhone']:
                raise Exception('One of ReceiverPhone and ReceiverCellPhone is required.') 
            
        
        
        #若物流交易編號(AllPayLogisticsID)為空值時，收件人郵遞區號(ReceiverZipCode)不可為空。
        ValidateZipCode('ReceiverZipCode', PostParams['ReceiverZipCode'], IsAllowEmpty) 
        
        #若物流交易編號(AllPayLogisticsID)為空值時，收件人地址(ReceiverAddress)不可為空。
        ValidateAddress('ReceiverAddress', PostParams['ReceiverAddress'], 6, 60, IsAllowEmpty) 

        if PostParams['LogisticsSubType'] == LogisticsSubType.ECAN and PostParams['Temperature'] != Temperature.ROOM:
            #物流子類型為宅配通(ECAN)時，溫層(Temperature)只能用常溫(ROOM)
            raise Exception('Temperature should be ROOM when LogisticsSubType is ECAN.') 
        

        if PostParams['LogisticsSubType'] == LogisticsSubType.ECAN and date('Ymd', strtotime(PostParams['ScheduledDeliveryDate'])) < date('Ymd', strtotime('+3 day')):
            #指定送達日期為該訂單建立時間 + 3 天
            raise Exception('ScheduledDeliveryDate should be the time that create order + 3 day.') 
        

        ValidateAmount('GoodsAmount', PostParams['GoodsAmount']) 
        if PostParams['GoodsAmount'] < MinAmount or PostParams['GoodsAmount'] > MaxAmount:
            raise Exception('Invalid GoodsAmount.') 
        			
        ValidateString('GoodsName', PostParams['GoodsName'], 60, true) 
        ValidateTemperature() 
        ValidateDistance() 
        ValidateSpecification() 
        ValidateScheduledDeliveryTime(true) 
        ValidateString('Remark', PostParams['Remark'], 200, true) 
        
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        #解析回傳結果
        #正確：1|OK
        #錯誤：0|ErrorMessage
        Feedback = ECPay_IO.ServerPost(PostParams, ServiceURL) 
        Result = ParseFeedback(Feedback)
        
        return Result 
    
    
    
    #  超商取貨逆物流訂單(統一超商B2C)
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def CreateUnimartB2CReturnOrder():
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'AllPayLogisticsID':'',
            'ServerReplyURL':'',
            'GoodsName':'',
            'GoodsAmount':0,
            'SenderName':'',
            'SenderPhone':'',
            'Remark':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        PostParams['CollectionAmount'] = 0 
        PostParams['ServiceType'] = 4 #退貨不付款
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('UNIMART_RETURN_ORDER') 
        ValidateID('AllPayLogisticsID', PostParams['AllPayLogisticsID'], 20, true) 
        ValidateURL('ServerReplyURL', PostParams['ServerReplyURL']) 
        ValidateString('GoodsName', PostParams['GoodsName'], 60, true) 
        ValidateAmount('GoodsAmount', PostParams['GoodsAmount']) 
        ValidateString('SenderName', PostParams['SenderName'], 50) 
        ValidatePhoneNumber('SenderPhone', PostParams['SenderPhone'], true) 
        ValidateString('Remark', PostParams['Remark'], 20, true) 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 

        MinAmount = 1  #金額下限
        MaxAmount = 19999  #金額上限
        if PostParams['GoodsAmount'] < MinAmount or PostParams['GoodsAmount'] > MaxAmount:
            raise Exception('Invalid GoodsAmount.') 
        	
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        #解析回傳結果
        #正確：RtnMerchantTradeNo | RtnOrderNo
        #錯誤：|ErrorMessage
        Feedback = ECPay_IO.ServerPost(PostParams, ServiceURL) 
        Pieces = explode('|', Feedback) 
        Result = {'RtnMerchantTradeNo':'', 'RtnOrderNo':''}
        if Pieces[0]:
            Result = {'ErrorMessage':Pieces[1]}
        else:
            Result['RtnMerchantTradeNo'] = Pieces[0] 
            Result['RtnOrderNo'] = Pieces[1] 
        
        
        return Result 
    

    
    #  超商取貨逆物流訂單(萊爾富超商B2C)
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def CreateHiLifeB2CReturnOrder():
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'AllPayLogisticsID':'',
            'ServerReplyURL':'',
            'GoodsName':'',
            'GoodsAmount':0,
            'SenderName':'',
            'SenderPhone':'',
            'Remark':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        PostParams['CollectionAmount'] = 0 
        PostParams['ServiceType'] = 4 #退貨不付款
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('HILIFE_RETURN_ORDER') 
        ValidateID('AllPayLogisticsID', PostParams['AllPayLogisticsID'], 20, true) 
        ValidateURL('ServerReplyURL', PostParams['ServerReplyURL']) 
        ValidateString('GoodsName', PostParams['GoodsName'], 60, true) 
        ValidateAmount('GoodsAmount', PostParams['GoodsAmount']) 
        ValidateString('SenderName', PostParams['SenderName'], 50) 
        ValidatePhoneNumber('SenderPhone', PostParams['SenderPhone'], true) 
        ValidateString('Remark', PostParams['Remark'], 20, true) 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 

        MinAmount = 1  #金額下限
        MaxAmount = 20000  #金額上限
        if PostParams['GoodsAmount'] < MinAmount or PostParams['GoodsAmount'] > MaxAmount:
            raise Exception('Invalid GoodsAmount.') 
        	
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        #解析回傳結果
        #正確：RtnMerchantTradeNo | RtnOrderNo
        #錯誤：|ErrorMessage
        Feedback = ECPay_IO.ServerPost(PostParams, ServiceURL) 
        Pieces = explode('|', Feedback) 
        Result = {'RtnMerchantTradeNo':'', 'RtnOrderNo':''}
        if Pieces[0]:
            Result = {'ErrorMessage':Pieces[1]} 
        else:
            Result['RtnMerchantTradeNo'] = Pieces[0] 
            Result['RtnOrderNo'] = Pieces[1] 
        
        
        return Result 
    

    
    #  超商取貨逆物流訂單(全家超商B2C)
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def CreateFamilyB2CReturnOrder():
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'AllPayLogisticsID':'',
            'ServerReplyURL':'',
            'GoodsName':'',
            'GoodsAmount':0,
            'SenderName':'',
            'SenderPhone':'',
            'Remark':'',
            'Quantity':'',
            'Cost':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        PostParams['CollectionAmount'] = 0 
        PostParams['ServiceType'] = 4 #退貨不付款
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('FAMILY_RETURN_ORDER') 
        ValidateID('AllPayLogisticsID', PostParams['AllPayLogisticsID'], 20, true) 
        ValidateURL('ServerReplyURL', PostParams['ServerReplyURL']) 
        ValidateString('GoodsName', PostParams['GoodsName'], 50, true) 
        ValidateAmount('GoodsAmount', PostParams['GoodsAmount']) 
        ValidateString('SenderName', PostParams['SenderName'], 50) 
        ValidatePhoneNumber('SenderPhone', PostParams['SenderPhone'], true) 
        ValidateString('Remark', PostParams['Remark'], 20, true) 
        ValidateString('Quantity', PostParams['Quantity'], 50, true) 
        ValidateString('Cost', PostParams['Cost'], 50, true) 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #檢查商品名稱, 數量 與 成本
        GoodsNameNumber = count(explode('#', PostParams['GoodsName'])) 
        QuantityNumber = count(explode('#', PostParams['Quantity'])) 
        CostNumber = count(explode('#', PostParams['Cost'])) 
        
        if not PostParams['GoodsName'] and PostParams['Quantity']:
            if GoodsNameNumber != QuantityNumber:
                raise Exception('GoodsName number and Quantity number do not match.') 
            
        
        
        if not PostParams['Quantity'] and PostParams['Cost']:
            if GoodsNameNumber != CostNumber:
                raise Exception('Quantity number and Cost number do not match.') 
            
        
        
        if not PostParams['Cost'] and PostParams['GoodsName']:
            if GoodsNameNumber != CostNumber:
                raise Exception('Cost number and GoodsName number do not match.') 
            
        

        MinAmount = 1  #金額下限
        MaxAmount = 20000  #金額上限
        if PostParams['GoodsAmount'] < MinAmount or PostParams['GoodsAmount'] > MaxAmount:
            raise Exception('Invalid GoodsAmount.') 
        	
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        #解析回傳結果
        #正確：RtnMerchantTradeNo | RtnOrderNo
        #錯誤：|ErrorMessage
        Feedback = ECPay_IO.ServerPost(PostParams, ServiceURL) 
        Pieces = explode('|', Feedback) 
        Result = {'RtnMerchantTradeNo':'', 'RtnOrderNo':''} 
        if Pieces[0]:
            Result = {'ErrorMessage':Pieces[1]} 
        else:
            Result['RtnMerchantTradeNo'] = Pieces[0] 
            Result['RtnOrderNo'] = Pieces[1] 
        
        
        return Result 
    
    
    
    #  全家逆物流核帳(全家超商B2C)
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def CheckFamilyB2CLogistics():
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'RtnMerchantTradeNo':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('FAMILY_RETURN_CHECK') 
        ValidateID('RtnMerchantTradeNo', PostParams['RtnMerchantTradeNo'], 13) 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        #解析回傳結果
        #正確：1|OK
        #錯誤：0|ErrorMessage
        Feedback = ECPay_IO.ServerPost(PostParams, ServiceURL) 
        Result = ParseFeedback(Feedback)
        
        return Result 
    

    
    #  廠商修改出貨日期、取貨門市(統一超商B2C)
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def UpdateUnimartLogisticsInfo():
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'AllPayLogisticsID':'',
            'ShipmentDate':'',
            'ReceiverStoreID':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('UNIMART_UPDATE_LOGISTICS_INFO') 
        ValidateID('AllPayLogisticsID', PostParams['AllPayLogisticsID'], 20) 
        
        ValidateShipmentDate(true) 
        ValidateMixTypeID('ReceiverStoreID', PostParams['ReceiverStoreID'], 6, true) 
        if PostParams['ShipmentDate'] and PostParams['ReceiverStoreID']:
            raise Exception('ShipmentDate or ReceiverStoreID is required.') 
        
        
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        #解析回傳結果
        #正確：1|OK
        #錯誤：0|ErrorMessage
        Feedback = ECPay_IO.ServerPost(PostParams, ServiceURL) 
        Result = ParseFeedback(Feedback)
        
        return Result 
    

    
    #  更新門市(統一超商C2C)
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def UpdateUnimartStore():
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'AllPayLogisticsID':'',
            'CVSPaymentNo':'',
            'CVSValidationNo':'',
            'StoreType':'',
            'ReceiverStoreID':'',
            'ReturnStoreID':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('UNIMART_UPDATE_STORE_INFO') 
        ValidateID('AllPayLogisticsID', PostParams['AllPayLogisticsID'], 20) 
        ValidateMixTypeID('CVSPaymentNo', PostParams['CVSPaymentNo'], 15) 
        ValidateID('CVSValidationNo', PostParams['CVSValidationNo'], 10) 
        ValidateStoreType() 
        
        if PostParams['StoreType'] == StoreType.RECIVE_STORE:
            ValidateMixTypeID('ReceiverStoreID', PostParams['ReceiverStoreID'], 6) 
        else:
            unset(PostParams['ReceiverStoreID']) 
        
    
        if PostParams['StoreType'] == StoreType.RETURN_STORE:
            ValidateMixTypeID('ReturnStoreID', PostParams['ReturnStoreID'], 6) 
        else:
            unset(PostParams['ReturnStoreID']) 
        
        
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        #解析回傳結果
        #正確：1|OK
        #錯誤：0|ErrorMessage
        Feedback = ECPay_IO.ServerPost(PostParams, ServiceURL) 
        Result = ParseFeedback(Feedback)
        
        return Result 
    
    
    
    #  取消訂單(統一超商C2C)
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def CancelUnimartLogisticsOrder():
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'AllPayLogisticsID':'',
            'CVSPaymentNo':'',
            'CVSValidationNo':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('UNIMART_CANCEL_LOGISTICS_ORDER') 
        ValidateID('AllPayLogisticsID', PostParams['AllPayLogisticsID'], 20) 
        ValidateMixTypeID('CVSPaymentNo', PostParams['CVSPaymentNo'], 15) 
        ValidateID('CVSValidationNo', PostParams['CVSValidationNo'], 10) 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        #解析回傳結果
        #正確：1|OK
        #錯誤：0|ErrorMessage
        Feedback = ECPay_IO.ServerPost(PostParams, ServiceURL) 
        Result = ParseFeedback(Feedback)
        
        return Result 
    
    
    
    #  物流訂單查詢
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def QueryLogisticsInfo():
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'AllPayLogisticsID':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        PostParams['TimeStamp'] = strtotime('now') 
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('QUERY_LOGISTICS_INFO') 
        ValidateID('AllPayLogisticsID', PostParams['AllPayLogisticsID'], 20) 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        #解析回傳結果
        #回應訊息：MerchantID=XXX&MerchantTradeNo=XXX&AllPayLogisticsID=XXX&GoodsAmount=XXX&LogisticsType=XXX&HandlingCharge=XXX&TradeDate=XXX&LogisticsStatus=XXX&GoodsName=XXX &CheckMacValue=XXX
        Result = {} 
        Feedback = ECPay_IO.ServerPost(PostParams, ServiceURL) 
        parse_str(Feedback, Result) 
        
        return Result 
    
    
    
    #  產生托運單(宅配)/一段標(超商取貨)
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @param		String ButtonDesc 按鈕顯示名稱
    # @param		String Target 表單 action 目標
    # @return		String
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def PrintTradeDoc(ButtonDesc = '產生托運單/一段標', Target = '_blank'):
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'AllPayLogisticsID':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('PRINT_TRADE_DOC') 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        return GenPostHTML(ButtonDesc, Target) 
    
    
    
    #  列印繳款單(統一超商C2C)
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @param		String ButtonDesc 按鈕顯示名稱
    # @param		String Target 表單 action 目標
    # @return		String
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def PrintUnimartC2CBill(ButtonDesc = '列印繳款單(統一超商C2C)', Target = '_blank'):
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'AllPayLogisticsID':'',
            'CVSPaymentNo':'',
            'CVSValidationNo':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('PRINT_UNIMART_C2C_BILL') 
        ValidateID('AllPayLogisticsID', PostParams['AllPayLogisticsID'], 20) 
        ValidateMixTypeID('CVSPaymentNo', PostParams['CVSPaymentNo'], 15) 
        ValidateID('CVSValidationNo', PostParams['CVSValidationNo'], 10) 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        return GenPostHTML(ButtonDesc, Target) 
    

    
    #  全家列印小白單(全家超商C2C)
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @param		String ButtonDesc 按鈕顯示名稱
    # @param		String Target 表單 action 目標
    # @return		String
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def PrintFamilyC2CBill(ButtonDesc = '全家列印小白單(全家超商C2C)', Target = '_blank'):
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'AllPayLogisticsID':'',
            'CVSPaymentNo':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('PRINT_FAMILY_C2C_BILL') 
        ValidateID('AllPayLogisticsID', PostParams['AllPayLogisticsID'], 20) 
        ValidateMixTypeID('CVSPaymentNo', PostParams['CVSPaymentNo'], 15) 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        return GenPostHTML(ButtonDesc, Target) 
    
    
    
    #  萊爾富列印小白單(萊爾富超商C2C)
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @param		String ButtonDesc 按鈕顯示名稱
    # @param		String Target 表單 action 目標
    # @return		String
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def PrintHiLifeC2CBill(ButtonDesc = '萊爾富列印小白單(萊爾富超商C2C)', Target = '_blank'):
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'AllPayLogisticsID':'',
            'CVSPaymentNo':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('Print_HILIFE_C2C_BILL') 
        ValidateID('AllPayLogisticsID', PostParams['AllPayLogisticsID'], 20) 
        ValidateMixTypeID('CVSPaymentNo', PostParams['CVSPaymentNo'], 15) 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        return GenPostHTML(ButtonDesc, Target) 
    
    
    
    #  產生 B2C 測標資料
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK
    # @param		String ButtonDesc 按鈕顯示名稱
    # @param		String Target 表單 action 目標
    # @return		String
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def CreateTestData(ButtonDesc = '產生 B2C 測標資料', Target = '_blank'):
        
        #參數初始化
        ParamList = {
            'MerchantID':'',
            'ClientReplyURL':'',
            'LogisticsSubType':'',
            'PlatformID':''
        } 
        PostParams = GetPostParams(Send, ParamList) 
        
        #參數檢查
        ValidateHashKey() 
        ValidateHashIV() 
        ValidateID('MerchantID', PostParams['MerchantID'], 10) 
        ServiceURL = GetURL('CREATE_TEST_DATA') 
        ValidateLogisticsSubType() 
        ValidateID('PlatformID', PostParams['PlatformID'], 10, true) 
        
        #產生 CheckMacValue
        PostParams['CheckMacValue'] = ECPay_CheckMacValue.generate(PostParams, HashKey, HashIV) 
        
        return GenPostHTML(ButtonDesc, Target) 
    
    
    
    #  Hash Key 檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateHashKey():
        Name = 'HashKey'  #參數名稱
        Value = HashKey  #參數內容
        AllowEmpty = False  #是否允許空值
        
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        
    

    
    #  Hash IV 檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
    
    def ValidateHashIV():
        Name = 'HashIV'  #參數名稱
        Value = HashKey  #參數內容
        AllowEmpty = False  #是否允許空值
        
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        
    

    
    #  ID 檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Value		參數內容
    # @param		Integer	MaxLength	參數最大長度
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateID(Name, Value, MaxLength = 1, AllowEmpty = False):
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #格式檢查
            IsValidFormat(Name, '/^\d{1,'+MaxLength+'$/', Value) 
        
    
    

    #  URL 檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Value		參數內容
    # @param		Integer	MaxLength	參數最大長度
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateURL(Name, Value, MaxLength = 200, AllowEmpty = False):
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #格式檢查
            IsValidFormat(Name, '/^(http|https):\/\/+/', Value) 
            
            #長度檢查
            IsOverLength(Name, StringLength(Value, Encode), MaxLength) 
        
    
    
    
    #  字串檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Value		參數內容
    # @param		Integer	MaxLength	參數最大長度
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateString(Name, Value, MaxLength = 1, AllowEmpty = False):
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #長度檢查
            IsOverLength(Name, StringLength(Value, Encode), MaxLength) 
        
    
    
    
    #  金額檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Value		參數內容
    # @param		Integer	MaxLength	參數最大長度
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateAmount(Name, Value, AllowEmpty = False):
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #資料型態檢查
            IsInteger(Name, Value) 
            
            #格式檢查
            IsValidFormat(Name, '/^\d+$/', Value) 
        
    
    
    
    #  電話號碼檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Value		參數內容
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidatePhoneNumber(Name, Value, AllowEmpty = False):
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #格式檢查
            IsValidFormat(Name, '/^\(?\d{2\)?\-?\d{2,6\-?\d{2,6(#\d{1,6){0,1$/', Value) 
        
    

    
    #  手機號碼檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Value		參數內容
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateCellphoneNumber(Name, Value, AllowEmpty = False):
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #格式檢查
            IsValidFormat(Name, '/^09\d{8$/', Value) 
        
    
    
    
    #  電子郵件檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Value		參數內容
    # @param		Integer	MaxLength	參數最大長度
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateEmail(Name, Value, MaxLength = 100, AllowEmpty = False):
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #長度檢查
            IsOverLength(Name, StringLength(Value, Encode), MaxLength) 
            #格式檢查
            IsValidFormat(Name, '/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,4$/', Value) 
        
    
    
    
    #  郵遞區號檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Value		參數內容
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateZipCode(Name, Value, AllowEmpty = False):
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #格式檢查
            IsValidFormat(Name, '/^\d{3,5$/', Value) 
        
    
    
    
    #  地址檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Value		參數內容
    # @param		Integer	MinLength	參數最小限制長度
    # @param		Integer	MaxLength	參數最大限制長度
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateAddress(Name, Value, MinLength = 1, MaxLength = 1, AllowEmpty = False):
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #長度檢查

            if MinLength:
                #最小長度限制
                IsBelowLength(Name, StringLength(Value, Encode), MinLength) 
            
            if MaxLength:
                #最大長度限制
                IsOverLength(Name, StringLength(Value, Encode), MaxLength) 
            
        
    

    
    #  混合型態 ID 檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Value		參數內容
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateMixTypeID(Name, Value, MaxLength = 1, AllowEmpty = False):
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #格式檢查
            IsValidFormat(Name, '/^[0-9a-zA-Z]{1,'+MaxLength+'$/', Value) 
        
    
    
    
    
    
    #  門市類型檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateStoreType():
        Name = 'StoreType'  #參數名稱
        Value = PostParams['StoreType']  #參數內容
        ClassName = 'StoreType'  #合法資料 Class 名稱
        AllowEmpty = False  #是否允許空值
        
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #內容檢查
            IsLegalValue(Name, ClassName, Value) 
        
    

    
    #  廠商交易編號檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateMerchantTradeNo():
        Name = 'MerchantTradeNo'  #參數名稱
        Value = PostParams['MerchantTradeNo']  #參數內容
        AllowEmpty = False  #是否允許空值
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #格式檢查
            IsValidFormat(Name, '/^[a-zA-Z0-9]{1,20$/', Value) 
        
    
    
    
    #  物流類型檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateLogisticsType():
        Name = 'LogisticsType'  #參數名稱
        Value = PostParams['LogisticsType']  #參數內容
        ClassName = 'LogisticsType'  #合法資料 Class 名稱
        AllowEmpty = False  #是否允許空值
        
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #內容檢查
            IsLegalValue(Name, ClassName, Value) 
        
    
    
    
    #  物流子類型檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateLogisticsSubType(AllowEmpty = False):
        Name = 'LogisticsSubType'  #參數名稱
        Value = PostParams['LogisticsSubType']  #參數內容
        ClassName = 'LogisticsSubType'  #合法資料 Class 名稱
        
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            if isset(PostParams['LogisticsType']):
                LogisticsType = PostParams['LogisticsType'] 
                #宅配物流子類型檢查
                if LogisticsType == LogisticsType.HOME:
                    if Value != LogisticsSubType.TCAT and Value != LogisticsSubType.ECAN:
                        raise Exception('Invalid home delivery '+Name+'.') 
                    
                
                
                #超商取貨物流子類型檢查
                if LogisticsType == LogisticsType.CVS:
                    if Value != LogisticsSubType.FAMILY and Value != LogisticsSubType.UNIMART and Value != LogisticsSubType.HILIFE and Value != LogisticsSubType.FAMILY_C2C and Value != LogisticsSubType.UNIMART_C2C and Value != LogisticsSubType.HILIFE_C2C:
                        raise Exception('Invalid CVS pickup ' + Name + '.') 
            #物流類型無設定時的內容檢查
            IsLegalValue(Name, ClassName, Value) 
        
    
    

    #  是否代收貨款檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateIsCollection(AllowEmpty = False):
        Name = 'IsCollection'  #參數名稱
        Value = PostParams['IsCollection']  #參數內容
        ClassName = 'IsCollection'  #合法資料 Class 名稱
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #內容檢查
            IsLegalValue(Name, ClassName, Value) 
            #目前物流類型(LogisticsType)宅配(Home)不支援代收貨款(IsCollection = Y)
            if PostParams['LogisticsType'] == LogisticsType.HOME and Value == IsCollection.YES:
                raise Exception(Name + ' could not be Y, when LogisticsType is Home.') 
            
        
    
    
    
    #  使用設備檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateDevice(AllowEmpty = False):
        Name = 'Device'  #參數名稱
        Value = PostParams['Device']  #參數內容
        ClassName = 'Device'  #合法資料 Class 名稱
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #資料型態檢查
            IsInteger(Name, Value) 
            #內容檢查
            IsLegalValue(Name, ClassName, Value) 
        
    
    
    
    #  廠商交易時間檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateMerchantTradeDate():
        Name = 'MerchantTradeDate'  #參數名稱
        Value = PostParams['MerchantTradeDate']  #參數內容
        ClassName = 'MerchantTradeDate'  #合法資料 Class 名稱
        AllowEmpty = False  #是否允許空值
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #日期檢查
            IsDate(Name, 'Y/m/d H:i:s', Value) 
        
    

    
    #  溫層檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateTemperature():
        Name = 'Temperature'  #參數名稱
        Value = PostParams['Temperature']  #參數內容
        ClassName = 'Temperature'  #合法資料 Class 名稱
        AllowEmpty = False  #是否允許空值
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #內容檢查
            IsLegalValue(Name, ClassName, Value) 
        
    

    
    #  距離檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateDistance():
        Name = 'Distance'  #參數名稱
        Value = PostParams['Distance']  #參數內容
        ClassName = 'Distance'  #合法資料 Class 名稱
        AllowEmpty = False  #是否允許空值
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #內容檢查
            IsLegalValue(Name, ClassName, Value) 
        
    
    
    
    #  規格檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateSpecification():
        Name = 'Specification'  #參數名稱
        Value = PostParams['Specification']  #參數內容
        ClassName = 'Specification'  #合法資料 Class 名稱
        AllowEmpty = False  #是否允許空值
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #內容檢查
            IsLegalValue(Name, ClassName, Value) 
        
    
        
    
    #  預定送達時段檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateScheduledDeliveryTime(AllowEmpty = False):
        Name = 'ScheduledDeliveryTime'  #參數名稱
        Value = PostParams['ScheduledDeliveryTime']  #參數內容
        ClassName = 'ScheduledDeliveryTime'  #合法資料 Class 名稱
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #內容檢查
            IsLegalValue(Name, ClassName, Value) 
        
    
    
    
    #  物流訂單出貨日期檢查
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		Boolean	AllowEmpty	是否允許空值
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ValidateShipmentDate(AllowEmpty = False):
        Name = 'ShipmentDate'  #參數名稱
        Value = PostParams['ShipmentDate']  #參數內容
        ClassName = 'ShipmentDate'  #合法資料 Class 名稱
        if Value:
            #是否允許空值
            IsAllowName, AllowEmpty 
        else:
            #日期檢查
            IsDate(Name, 'Y/m/d', Value) 
        
    

    
    #  是否允許空值
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		boolean	AllowEmpty	是否允許空值
    # @return		boolean
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def IsAllowEmpty(IsAllowName, AllowEmpty):
        if not AllowEmpty:
            raise Exception(Name + ' is required.') 
        
    
        
    
    #  是否超過長度限制
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name			參數名稱
    # @param		Integer	Length			參數長度
    # @param		Integer	MaxLength 		參數限制長度
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def IsOverLength(Name, Length, MaxLength):
        if Length > MaxLength:
            raise Exception(Name + ' max length is ' + MaxLength + '.') 
        
    

    
    #  是否超過長度限制
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name			參數名稱
    # @param		Integer	Length			參數長度
    # @param		Integer	MinLength 		參數限制長度
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def IsBelowLength(Name, Length, MinLength):
        if Length < MinLength:
            raise Exception(Name + ' min length is ' + MinLength + '.') 
        
    
    
    
    #  是否為指定格式
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Pattern	格式檢查用正規表示法
    # @param		String	Value		參數內容
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def IsValidFormat(Name, Pattern, Value):
        if not Value:
            if not preg_match(Pattern, Value):
                raise Exception('Invalid ' + Name + '.') 
            
        
    
    
    
    #  是否為數值
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name		參數名稱
    # @param		String	Value		參數內容
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def IsInteger(Name, Value):
        if not is_int(Value):
            raise Exception(Name + ' type should be integer.') 
        
    
    
    
    #  是否為數值
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name			參數名稱
    # @param		String	ClassName		合法資料 Class 名稱
    # @param		String	Value			參數內容
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def IsLegalValue(Name, ClassName, Value):
        #取得合法資料內容
        ReflectionObject = ReflectionClass(ClassName) 
        ContentList = ReflectionObject.getConstants() 
        del ReflectionObject
        
        #檢查是否為合法資料
        if not Value in ContentList:
            raise Exception('Illegal ' + Name + '.') 
        
    
    
    #  是否為正確日期
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Validate
    # @param		String	Name			參數名稱
    # @param		String	Format			日期格式
    # @param		String	Value			參數內容
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def IsDate(Name, Format, Value):
        if date(Format, strtotime(Value)) != Value:
            raise Exception('Invalid ' + Name + '.') 
        
    
    
    
    #  取得並過濾 $_POST 參數
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK_Misc
    # @param		Array	Source			$_POST 參數來源
    # @param		Array	ParamList		合法參數與預設值
    # @param		Array	MergeParams	其他待合併參數
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def GetPostParams(Source, ParamList, MergeParams = {}):
        #過濾非法參數
        PostParams = {} 
        for Name,Value in ParamList.items():
            if isset(Source[Name]):
                PostParams[Name] = Source[Name] 
            else:
                #若未設定則帶預設值
                PostParams[Name] = Value 
        return array_merge(MergeParams, PostParams) 
    
    
    
    #  取得 ECPay URL
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK_Misc
    # @param		String	FunctionType	功能名稱
    # @return		String
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def GetURL(FunctionType):
        MerchantID = PostParams['MerchantID'] 
        UrlList = {} 
        if MerchantID == ECPayTestMerchantID.B2C or MerchantID == ECPayTestMerchantID.C2C:
            #測試環境
            UrlList = {
                'CVS_MAP':ECPayTestURL.CVS_MAP,
                'SHIPPING_ORDER':ECPayTestURL.SHIPPING_ORDER,
                'HOME_RETURN_ORDER':ECPayTestURL.HOME_RETURN_ORDER,
                'UNIMART_RETURN_ORDER':ECPayTestURL.UNIMART_RETURN_ORDER,
                'HILIFE_RETURN_ORDER':ECPayTestURL.HILIFE_RETURN_ORDER,
                'FAMILY_RETURN_ORDER':ECPayTestURL.FAMILY_RETURN_ORDER,
                'FAMILY_RETURN_CHECK':ECPayTestURL.FAMILY_RETURN_CHECK,
                'UNIMART_UPDATE_LOGISTICS_INFO':ECPayTestURL.UNIMART_UPDATE_LOGISTICS_INFO,
                'UNIMART_UPDATE_STORE_INFO':ECPayTestURL.UNIMART_UPDATE_STORE_INFO,
                'UNIMART_CANCEL_LOGISTICS_ORDER':ECPayTestURL.UNIMART_CANCEL_LOGISTICS_ORDER,
                'QUERY_LOGISTICS_INFO':ECPayTestURL.QUERY_LOGISTICS_INFO,
                'PRINT_TRADE_DOC':ECPayTestURL.PRINT_TRADE_DOC,
                'PRINT_UNIMART_C2C_BILL':ECPayTestURL.PRINT_UNIMART_C2C_BILL,
                'PRINT_FAMILY_C2C_BILL':ECPayTestURL.PRINT_FAMILY_C2C_BILL,
                'Print_HILIFE_C2C_BILL':ECPayTestURL.Print_HILIFE_C2C_BILL,
                'CREATE_TEST_DATA':ECPayTestURL.CREATE_TEST_DATA,
            }
        else:
            #正式環境
            UrlList = {
                'CVS_MAP':ECPayURL.CVS_MAP,
                'SHIPPING_ORDER':ECPayURL.SHIPPING_ORDER,
                'HOME_RETURN_ORDER':ECPayURL.HOME_RETURN_ORDER,
                'UNIMART_RETURN_ORDER':ECPayURL.UNIMART_RETURN_ORDER,
                'HILIFE_RETURN_ORDER':ECPayURL.HILIFE_RETURN_ORDER,
                'FAMILY_RETURN_ORDER':ECPayURL.FAMILY_RETURN_ORDER,
                'FAMILY_RETURN_CHECK':ECPayURL.FAMILY_RETURN_CHECK,
                'UNIMART_UPDATE_LOGISTICS_INFO':ECPayURL.UNIMART_UPDATE_LOGISTICS_INFO,
                'UNIMART_UPDATE_STORE_INFO':ECPayURL.UNIMART_UPDATE_STORE_INFO,
                'UNIMART_CANCEL_LOGISTICS_ORDER':ECPayURL.UNIMART_CANCEL_LOGISTICS_ORDER,
                'QUERY_LOGISTICS_INFO':ECPayURL.QUERY_LOGISTICS_INFO,
                'PRINT_TRADE_DOC':ECPayURL.PRINT_TRADE_DOC,
                'PRINT_UNIMART_C2C_BILL':ECPayURL.PRINT_UNIMART_C2C_BILL,
                'PRINT_FAMILY_C2C_BILL':ECPayURL.PRINT_FAMILY_C2C_BILL,
                'Print_HILIFE_C2C_BILL':ECPayURL.Print_HILIFE_C2C_BILL,
                'CREATE_TEST_DATA':ECPayURL.CREATE_TEST_DATA,
            } 
        return UrlList[FunctionType] 
    
    
    
    #  加入換行字元
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	Misc
    # @param		String	Content	內容
    # @return		String
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def AddNextLine(Content):
        return Content + PHP_EOL 
    
    
    
    #  產生自動/手動 POST 提交表單
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK_Misc
    # @param		String	ButtonDesc	按鈕顯示名稱
    # @param		String	Target		表單 action 目標
    # @return		String
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def GenPostHTML(ButtonDesc = '', Target = '_self'):
        PostHTML = AddNextLine('<div style="text-align:center ">') 
        PostHTML += AddNextLine('  <form id="ECPayForm" method="POST" action="' + ServiceURL + '" target="' + Target + '">') 
        for Name,Value in PostParams.items():
            PostHTML += AddNextLine('    <input type="hidden" name="' + Name + '" value="' + Value + '" />') 
        if not ButtonDesc:
            #手動
            PostHTML += AddNextLine('    <input type="submit" id="__paymentButton" value="' + ButtonDesc + '" />') 
        else:
            #自動
            PostHTML += AddNextLine('    <script>document.getElementById("ECPayForm").submit() </script>') 
        PostHTML += AddNextLine('  </form>') 
        PostHTML += AddNextLine('</div>') 
        return PostHTML 
    
    
    
        #  依編碼方式取得字串長度
        #
        # @author		David Chen <david2003542@gmail.com>
        # @category	Misc
        # @param		String	RetriveString	字串內容
        # @param		String	Encode 		字串編碼
        # @return		Integer
        # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def StringLength(RetriveString, Encode):
        return mb_strlen(RetriveString, Encode) 
    
    
    
    
    #  解析 ECPay 回傳結果
    #
    # @author		David Chen <david2003542@gmail.com>
    # @category	SDK_Misc
    # @param		String	Feedback		回傳結果
    # @param		Array	FeedbackList	合法回傳參數
    # @param		String	Separator		分隔符號
    # @return		Array
    # @version		GIT: <david2003542/ECPayLogistic_PYTHON>
        
    def ParseFeedback(Feedback, FeedbackList = ['RtnCode', 'RtnMsg'], Separator = '|'):
        Pieces = explode(Separator, Feedback) 
        Feedback = {} 
        #回傳參數檢查
        if count(Pieces) == count(FeedbackList):
            for Idx,Name in FeedbackList.items():
                Feedback[Name] = Pieces[Idx] 
        else:
            Feedback['ParseMsg'] = 'Unknown feedback : ' + Feedback   
        return Feedback 
    



class ECPay_CheckMacValue():
    # 產生檢查碼
    def generate(arParameters = {}, HashKey = '', HashIV = ''):
        sMacValue = ''  
        if isset(arParameters):
            unset(arParameters['CheckMacValue']) 
            uksort(arParameters, ['ECPay_CheckMacValue','merchantSort']) 
            #組合字串
            sMacValue = 'HashKey=' + HashKey  
            for key,value in arParameters.items():
                sMacValue += '&' + key + '=' + value  
            sMacValue += '&HashIV=' + HashIV  
            #URL Encode編碼     
            sMacValue = urlencode(sMacValue) 
            #轉成小寫
            sMacValue = strtolower(sMacValue) 
            #取代為與 dotNet 相符的字元
            sMacValue = ECPay_CheckMacValue.Replace_Symbol(sMacValue) 
            #編碼
            sMacValue = md5(sMacValue) 
            sMacValue = strtoupper(sMacValue) 
        return sMacValue  
        

        
        # 自訂排序使用
        
        def merchantSort(a,b):
            return strcasecmp(a, b) 
        

        
        # 參數內特殊字元取代
        # 傳入	sParameters	參數
        # 傳出	sParameters	回傳取代後變數
        
        def Replace_Symbol(sParameters):
            if not sParameters:
                sParameters = str_replace('%2D', '-', sParameters) 
                sParameters = str_replace('%2d', '-', sParameters) 
                sParameters = str_replace('%5F', '_', sParameters) 
                sParameters = str_replace('%5f', '_', sParameters) 
                sParameters = str_replace('%2E', '.', sParameters) 
                sParameters = str_replace('%2e', '.', sParameters) 
                sParameters = str_replace('%21', '!', sParameters) 
                sParameters = str_replace('%2A', '#', sParameters) 
                sParameters = str_replace('%2a', '#', sParameters) 
                sParameters = str_replace('%28', '(', sParameters) 
                sParameters = str_replace('%29', ')', sParameters) 
            return sParameters  
        

        
        # 參數內特殊字元還原
        # 傳入	sParameters	參數
        # 傳出	sParameters	回傳取代後變數
        
        def Replace_Symbol_Decode(sParameters):
            if not sParameters:
                sParameters = str_replace('-', '%2d', sParameters) 
                sParameters = str_replace('_', '%5f', sParameters) 
                sParameters = str_replace('.', '%2e', sParameters) 
                sParameters = str_replace('!', '%21', sParameters) 
                sParameters = str_replace('#', '%2a', sParameters) 
                sParameters = str_replace('(', '%28', sParameters) 
                sParameters = str_replace(')', '%29', sParameters) 
                sParameters = str_replace('+', '%20', sParameters) 
            return sParameters  
        
    



class ECPay_IO():
    def ServerPost(parameters ,ServiceURL):
        sSend_Info = ''  
        #組合字串
        for key,value in parameters.items():
            if sSend_Info == '':
                sSend_Info += key + '=' + value  
            else:
                sSend_Info += '&' + key + '=' + value  
            
        ch = curl_init() 

        if False == ch:
            raise Exception('curl failed to initialize') 

        curl_setopt(ch, CURLOPT_URL, ServiceURL) 
        curl_setopt(ch, CURLOPT_HEADER, False) 
        curl_setopt(ch, CURLOPT_RETURNTRANSFER, TRUE) 
        curl_setopt(ch, CURLOPT_SSL_VERIFYPEER, TRUE) 
        curl_setopt(ch, CURLOPT_POST, TRUE) 
        curl_setopt(ch, CURLOPT_POSTFIELDS, sSend_Info) 
        rs = curl_exec(ch) 

        if False == rs:
            raise Exception(curl_error(ch), curl_errno(ch)) 
        

        curl_close(ch) 
        return rs 
        
    

