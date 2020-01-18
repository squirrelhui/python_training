# try :
#     num = int(input('number: '))
#     result = 100 / num
#     print(result)
#     print('Done')
# except ValueError:
#     print('只接受数字')
# except ZeroDivisionError:
#     print('不能输入0')
# except EOFError:
#     print('不要CTRL+D')
# except KeyboardInterrupt:
#     print('不要CTRL+C')

# try :
#     num = int(input('number: '))
#     result = 100 / num
#     print(result)
#     print('done')
# except ValueError:
#     print('只接受数字')
# except ZeroDivisionError:
#     print('不能输入0')
# except EOFError:
#     print('\n886')
# except KeyboardInterrupt:
#     print('\n886')

# try :
#     num = int(input('number: '))
#     result = 100 / num
#     print(result)
#     print('done')
# except (KeyboardInterrupt, EOFError):
#     print('\n886: ')
# except (ValueError, ZeroDivisionError) as e:
#     print('只接受非零数字', e)

# try :
#     num = int(input('number: '))
#     result = 100 / num
#
# except (KeyboardInterrupt, EOFError):
#     print('\n886: ')
#     exit(101)
# except (ValueError, ZeroDivisionError) as e:
#     print('只接受非零数字', e)
#
# else:
#     print(result)
#
# print('done')

# try :
#     num = int(input('number: '))
#     result = 100 / num
#
# except (ValueError, ZeroDivisionError) as e:
#     print('只接受非0数字', e)
# except (KeyboardInterrupt, EOFError):
#     print('\n886')
#     exit(512)
# else:
#     print(result)
# finally:
#     print('done')